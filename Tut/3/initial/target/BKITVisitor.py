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


    # Visit a parse tree produced by BKITParser#var_declaration.
    def visitVar_declaration(self, ctx:BKITParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_type.
    def visitVar_type(self, ctx:BKITParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#id_list.
    def visitId_list(self, ctx:BKITParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declaration.
    def visitFunc_declaration(self, ctx:BKITParser.Func_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param_declaration.
    def visitParam_declaration(self, ctx:BKITParser.Param_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_of_params.
    def visitList_of_params(self, ctx:BKITParser.List_of_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_of_non_null_params.
    def visitList_of_non_null_params(self, ctx:BKITParser.List_of_non_null_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stament.
    def visitStament(self, ctx:BKITParser.StamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment_stament.
    def visitAssignment_stament(self, ctx:BKITParser.Assignment_stamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
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


    # Visit a parse tree produced by BKITParser#operands.
    def visitOperands(self, ctx:BKITParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sub_expression.
    def visitSub_expression(self, ctx:BKITParser.Sub_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stament.
    def visitCall_stament(self, ctx:BKITParser.Call_stamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression_list.
    def visitExpression_list(self, ctx:BKITParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#non_null_expression_list.
    def visitNon_null_expression_list(self, ctx:BKITParser.Non_null_expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stament.
    def visitReturn_stament(self, ctx:BKITParser.Return_stamentContext):
        return self.visitChildren(ctx)



del BKITParser