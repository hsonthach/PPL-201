from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from dataclasses import dataclass


class Raiser:
    def __init__(self, e: Exception):
        raise e


@dataclass
class Symbol:
    pass


class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        self.visit(self.ast, None)

    def visitProgram(self, ctx: Program, o):
        o = []
        exp = ctx.exp
        decl_list = ctx.decl
        for decl in decl_list:
            self.visit(decl, o)
        self.visit(exp, o)

    def visitVarDecl(self, ctx: VarDecl, o):
        o.append(ctx)

    def visitBinOp(self, ctx: BinOp, o):
        left = ctx.e1
        right = ctx.e2
        literals = [BoolType, FloatType, IntType]
        # recursive left & right till it become literals
        while not (type(left) in literals):
            left = self.visit(left, o)
        while not (type(right) in literals):
            right = self.visit(right, o)

        if (ctx.op in ["+", "-", "*"]):
            # Check TypeMismatchInExpression
            if (not (type(left) in [FloatType, IntType])) or (not (type(right) in [FloatType, IntType])):
                raise TypeMismatchInExpression(ctx)
            # Output
            if (type(left) is FloatType or type(right) is FloatType):
                return FloatType()
            return IntType()

        elif (ctx.op in ["/"]):
            # Check TypeMismatchInExpression
            if (not (type(left) in [FloatType, IntType])) or (not (type(right) in [FloatType, IntType])):
                raise TypeMismatchInExpression(ctx)
            # Output
            return FloatType()

        elif (ctx.op in ['&&', '||']):
            # Check TypeMismatchInExpression
            if (not (type(left) in [BoolType])) or (not (type(right) in [BoolType])):
                raise TypeMismatchInExpression(ctx)
            # Output
            return BoolType()

        elif (ctx.op in ["<", '>', '==', '!=']):
            # Check TypeMismatchInExpression
            if (not (type(left) is type(right))):
                raise TypeMismatchInExpression(ctx)
            # Output
            return BoolType()

    def visitUnOp(self, ctx: UnOp, o):
        val = ctx.e
        literals = [BoolType, FloatType, IntType]
        # recursive left & right till it become literals
        while not (type(val) in literals):
            val = self.visit(val, o)

        if (ctx.op in ['!']):
            # Check TypeMismatchInExpression
            if (not (type(val) in [BoolType])):
                raise TypeMismatchInExpression(ctx)
            # Output
            return BoolType()
        elif (ctx.op in ["-"]):
            # Check TypeMismatchInExpression
            if (not (type(val) in [FloatType, IntType])):
                raise TypeMismatchInExpression(ctx)
            # Output
            if (type(val) is FloatType):
                return FloatType()
            return IntType()

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx, o):
        return BoolType()

    def visitId(self, ctx, o):
        if not ([el.typ for el in o if ctx.name == el.name]):
            raise UndeclaredIdentifier(ctx.name)
        for el in o:
            if ctx.name == el.name:
                return el.typ
