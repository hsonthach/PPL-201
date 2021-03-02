from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce


class ASTGeneration(BKITVisitor):

    def visitProgram(self, ctx: BKITParser.ProgramContext):

        return ctx.exp().accept(self)

    def visitExp(self, ctx: BKITParser.ExpContext):
        # a := b := 4
        # Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))
        # [4,b,a]
        terms = list(reversed(list(map(lambda x: x.accept(self), ctx.term()))))
        # print(terms)

        def binaryGen(a, b):
            # 4 ,b
            return Binary(ctx.ASSIGN(0).getText(), b, a)
        #print(reduce(binaryGen, terms))
        return reduce(binaryGen, terms)

    def visitTerm(self, ctx: BKITParser.TermContext):
        if (ctx.getChildCount() == 1):
            return ctx.factor(0).accept(self)
        return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self))

    def visitFactor(self, ctx: BKITParser.FactorContext):
        operands = list(map(lambda x: x.accept(self), ctx.operand()))

        def binaryGen(a, b):

            return Binary(ctx.ANDOR(0).getText(), b, a)
        #print(reduce(binaryGen, terms))
        return reduce(binaryGen, operands)

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
