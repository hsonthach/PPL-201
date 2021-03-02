# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#global_vardecl.
    def visitGlobal_vardecl(self, ctx:BKITParser.Global_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardecl_list.
    def visitVardecl_list(self, ctx:BKITParser.Vardecl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl.
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_decllist.
    def visitPara_decllist(self, ctx:BKITParser.Para_decllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_decl.
    def visitPara_decl(self, ctx:BKITParser.Para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_decl.
    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmtList.
    def visitStmtList(self, ctx:BKITParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifStmt.
    def visitIfStmt(self, ctx:BKITParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elifStmt.
    def visitElifStmt(self, ctx:BKITParser.ElifStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseStmt.
    def visitElseStmt(self, ctx:BKITParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#whileStmt.
    def visitWhileStmt(self, ctx:BKITParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:BKITParser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forStmt.
    def visitForStmt(self, ctx:BKITParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callStmt.
    def visitCallStmt(self, ctx:BKITParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#breakStmt.
    def visitBreakStmt(self, ctx:BKITParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continueStmt.
    def visitContinueStmt(self, ctx:BKITParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnStmt.
    def visitReturnStmt(self, ctx:BKITParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argulist.
    def visitArgulist(self, ctx:BKITParser.ArgulistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcCall.
    def visitFuncCall(self, ctx:BKITParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignStmt.
    def visitAssignStmt(self, ctx:BKITParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#lhs.
    def visitLhs(self, ctx:BKITParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_exp.
    def visitIndex_exp(self, ctx:BKITParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operands.
    def visitOperands(self, ctx:BKITParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_literal.
    def visitArray_literal(self, ctx:BKITParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#number.
    def visitNumber(self, ctx:BKITParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primitive_types.
    def visitPrimitive_types(self, ctx:BKITParser.Primitive_typesContext):
        return self.visitChildren(ctx)



del BKITParser