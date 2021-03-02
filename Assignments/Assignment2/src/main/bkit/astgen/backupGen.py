from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

from functools import reduce


def destructure_list(list):
    return reduce(lambda a, b: a + b, list, [])


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        # [VarDecl(a,[1].{1,2.5})]
        # [VarDecl(b,[],2)]
        var_declare_list = []
        # [FuncDecl(foo,n,x[3],([VarDecl(a,[3,1].{{1},{1},{2.5}})].))]
        func_declare_list = []
        if (ctx.var_declare(0) != None):
            var_declare_list = destructure_list(list(
                map(lambda x: x.accept(self), ctx.var_declare())))
        if (ctx.func_declare(0) != None):
            func_declare_list = list(
                map(lambda x: x.accept(self), ctx.func_declare()))
        return Program(var_declare_list + func_declare_list)

    def visitVar_declare(self, ctx: BKITParser.ProgramContext):
        return ctx.variable_assign_list().accept(self)

    # Ex : a,b=5,c = 6,d[3]
    def visitVariable_assign_list(self, ctx: BKITParser.ProgramContext):
        # [VarDecl(a,[int,float].{1,2.5}),VarDecl(b,[int,float].{1,2.5})]
        variable_assign_list = list(
            map(lambda x: x.accept(self), ctx.variable_assign()))
        return variable_assign_list

    # Ex: a = 5  # a[5] = {1,2,3}
    def visitVariable_assign(self, ctx: BKITParser.ProgramContext):
        variable = ctx.variable().accept(self)
        # variable ASSIGN literals
        if (ctx.getChildCount() == 3):
            literal = ctx.literal().accept(self)
            return VarDecl(variable['id'], variable['dimension'], ctx.literal().accept(self))
        # variable
        return VarDecl(variable['id'], variable['dimension'],  None)

    def visitVariable(self, ctx: BKITParser.ProgramContext):
        variable = {
            "id": Id(''),
            "dimension": [],
        }
        # a
        if (ctx.ID()):
            variable['id'] = Id(ctx.ID().getText())
            return variable
        # a[3][4]
        variable = ctx.array_type().accept(self)
        return variable

    def visitArray_type(self, ctx: BKITParser.ProgramContext):
        variable = {
            "id": Id(ctx.ID().getText()),
            "dimension": [],
        }
        # calc dimension
        listOfDimension = list(
            map(lambda x: int(x.getText(), 0), ctx.INTEGER_LITERAL()))
        variable['dimension'] = listOfDimension

        return variable

    def visitLiteral(self, ctx: BKITParser.ProgramContext):
        if (ctx.INTEGER_LITERAL()):
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText(), 0))
        if (ctx.FLOAT_LITERAL()):
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        if (ctx.STRING_LITERAL()):
            return StringLiteral(ctx.STRING_LITERAL().getText())
        if (ctx.array_literal()):
            return ctx.array_literal().accept(self)
        return ctx.bool_literal().accept(self)

    def visitArray_literal(self, ctx: BKITParser.ProgramContext):
        literal_list = list(map(lambda x: x.accept(self), ctx.literal()))
        return ArrayLiteral(literal_list)

    def visitBool_literal(self, ctx: BKITParser.ProgramContext):
        if (ctx.getText() == 'True'):
            return BooleanLiteral(True)
        return BooleanLiteral(False)

    def visitFunc_declare(self, ctx: BKITParser.ProgramContext):
        id = Id(ctx.ID().getText())

        param_list = []
        if (ctx.param_declare()):
            param_list = ctx.param_declare().accept(self)

        tuple_statement = ctx.body().accept(self)

        return FuncDecl(id, param_list, tuple_statement)

    def visitParam_declare(self, ctx: BKITParser.ProgramContext):
        return ctx.param_list().accept(self)

    def visitParam_list(self, ctx: BKITParser.ProgramContext):
        variable_list = list(map(lambda x: x.accept(self), ctx.variable()))
        return list(map(lambda variable: VarDecl(variable['id'], variable['dimension'], None), variable_list))

    def visitBody(self, ctx: BKITParser.ProgramContext):
        return ctx.list_statement().accept(self)

    def visitList_statement(self, ctx: BKITParser.ProgramContext):
        var_declare_list = []
        statement_list = []

        var_declare_list = destructure_list(list(
            map(lambda x: x.accept(self), ctx.var_declare())))

        statement_list = list(map(lambda x: x.accept(self), ctx.statement()))

        return (var_declare_list, statement_list)

    def visitStatement(self, ctx: BKITParser.ProgramContext):
        return ctx.getChild(0).accept(self)

    def visitAssignment_stmt(self, ctx: BKITParser.ProgramContext):
        return ctx.assign_body().accept(self)

    def visitAssign_body(self, ctx: BKITParser.ProgramContext):
        return Assign(ctx.assign_head().accept(self), ctx.exp().accept(self))

    def visitAssign_head(self, ctx: BKITParser.ProgramContext):
        if (ctx.ID() != None):
            return Id(ctx.ID().getText())
        return ctx.index_exp().accept(self)

    def visitIf_stmt(self, ctx: BKITParser.ProgramContext):
        list_stmt = ctx.list_statement().accept(self)
        ifthen_stmt = [(ctx.exp().accept(self), list_stmt[0], list_stmt[1])]
        else_if_stmt = list(map(lambda x: x.accept(self), ctx.else_if_stmt()))
        else_stmt = ([], [])
        if (ctx.else_stmt()):
            else_stmt = ctx.else_stmt().accept(self)
        return If(ifthen_stmt + else_if_stmt, else_stmt)

    def visitElse_stmt(self, ctx: BKITParser.ProgramContext):
        return ctx.list_statement().accept(self)

    def visitElse_if_stmt(self, ctx: BKITParser.ProgramContext):
        list_stmt = ctx.list_statement().accept(self)
        return (ctx.exp().accept(self), list_stmt[0], list_stmt[1])

    def visitFor_stmt(self, ctx: BKITParser.ProgramContext):
        id = Id(ctx.ID().getText())
        # [exp1,exp2,exp3]
        exp_list = list(map(lambda x: x.accept(self), ctx.exp()))
        list_stmt = ctx.list_statement().accept(self)
        return For(id,  exp_list[0], exp_list[1], exp_list[2], list_stmt)

    def visitWhile_stmt(self, ctx: BKITParser.ProgramContext):
        list_stmt = ctx.list_statement().accept(self)
        return While(ctx.exp().accept(self), list_stmt)

    def visitDo_while_stmt(self, ctx: BKITParser.ProgramContext):
        list_stmt = ctx.list_statement().accept(self)
        return Dowhile(list_stmt, ctx.exp().accept(self))

    def visitBreak_stmt(self, ctx: BKITParser.ProgramContext):
        return Break()

    def visitContinue_stmt(self, ctx: BKITParser.ProgramContext):
        return Continue()

    def visitReturn_stmt(self, ctx: BKITParser.ProgramContext):
        exp = None
        if (ctx.exp()):
            exp = ctx.exp().accept(self)
        return Return(exp)

    def visitCall_stmt(self, ctx: BKITParser.ProgramContext):
        exps_list = ctx.exps_list().accept(self)
        return CallStmt(Id(ctx.ID().getText()), exps_list)

    def visitExp(self, ctx: BKITParser.ProgramContext):
        # exp1
        if (ctx.getChildCount() == 1):
            return ctx.exp1(0).accept(self)
        # exp1 INT_EQ exp1
        return BinaryOp(ctx.getChild(1).getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))

    def visitExp1(self, ctx: BKITParser.ProgramContext):
        # exp3
        if (ctx.getChildCount() == 1):
            return ctx.exp2().accept(self)
        # exp1 AND exp2
        return BinaryOp(ctx.getChild(1).getText(), ctx.exp1().accept(self), ctx.exp2().accept(self))

    def visitExp2(self, ctx: BKITParser.ProgramContext):
        if (ctx.getChildCount() == 1):
            return ctx.exp3().accept(self)
        return BinaryOp(ctx.getChild(1).getText(), ctx.exp2().accept(self), ctx.exp3().accept(self))

    def visitExp3(self, ctx: BKITParser.ProgramContext):
        # right association should be calced first ?
        if (ctx.getChildCount() == 1):
            return ctx.exp4().accept(self)
        return BinaryOp(ctx.getChild(1).getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))

    def visitExp4(self, ctx: BKITParser.ProgramContext):
        if (ctx.getChildCount() == 1):
            return ctx.exp5().accept(self)
            # return UnaryOp("[]", ArrayCell(None, [IntLiteral(value=34)]))
        return UnaryOp(ctx.getChild(0).getText(), ctx.exp4().accept(self))

    def visitExp5(self, ctx: BKITParser.ProgramContext):
        # index_exp
        if (ctx.getChildCount() == 1):
            return ctx.index_exp().accept(self)
        return UnaryOp(ctx.getChild(0).getText(), ctx.exp5().accept(self))

    def visitIndex_exp(self, ctx: BKITParser.ProgramContext):
        exp7 = ctx.exp7().accept(self)
        if (ctx.getChildCount() == 1):
            return exp7

        exp_list = list(map(lambda x: x.accept(self), ctx.exp()))

        return ArrayCell(exp7, exp_list)

    def visitExp7(self, ctx: BKITParser.ProgramContext):
        if (ctx.getChildCount() == 1):
            return ctx.exp8().accept(self)

        exps_list = ctx.exps_list().accept(self)
        return CallExpr(Id(ctx.ID().getText()), exps_list)

    def visitExps_list(self, ctx: BKITParser.ProgramContext):
        return list(map(lambda x: x.accept(self), ctx.exp()))

    def visitExp8(self, ctx: BKITParser.ProgramContext):
        if (ctx.ID()):
            return Id(ctx.ID().getText())

        if (ctx.getChildCount() == 3):
            return ctx.exp().accept(self)

        return ctx.literal().accept(self)
