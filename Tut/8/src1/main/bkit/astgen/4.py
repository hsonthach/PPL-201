from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):

    def visitProgram(self, ctx: BKITParser.ProgramContext):

        return ctx.exp().accept(self)

    def visitExp(self, ctx: BKITParser.ExpContext):
        # term
        if (ctx.getChildCount() == 1):
            return ctx.term().accept(self)
        # term ASSIGN exp
        return Binary(ctx.ASSIGN().getText(), ctx.term().accept(self), ctx.exp().accept(self))

    def visitTerm(self, ctx: BKITParser.TermContext):
        # factor
        if (ctx.getChildCount() == 1):
            # print(type(ctx.factor(0)))
            return ctx.factor(0).accept(self)
        # term ASSIGN exp
        return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self))

    def visitFactor(self, ctx: BKITParser.FactorContext):
        # operand
        if (ctx.getChildCount() == 1):
            return ctx.operand().accept(self)
        # term ASSIGN exp
        return Binary(ctx.ANDOR().getText(), ctx.factor().accept(self), ctx.operand().accept(self))

    def visitOperand(self, ctx: BKITParser.OperandContext):
        # '(' exp ')'
        if (ctx.getChildCount() == 3):
            return ctx.exp().accept(self)
        # ID | INTLIT | BOOLIT
        if (ctx.ID() != None):
            return Id(ctx.ID().getText())
        if (ctx.INTLIT() != None):
            return IntLiteral(ctx.INTLIT().getText())
        if (ctx.BOOLIT() != None):
            return BooleanLiteral(ctx.BOOLIT().getText())
