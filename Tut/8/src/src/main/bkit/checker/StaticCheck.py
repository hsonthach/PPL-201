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

    def visitBinOp(self, ctx: BinOp, o):
        o = []
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)
        while (type(left) is (BinOp or UnOp)):
            left = self.visit(left)
        while (type(right) is (BinOp or UnOp)):
            right = self.visit(right)

        if (ctx.op == "+" or ctx.op == "-" or ctx.op == "*"):
            # + -  *
            if ((not (type(left) is int or type(left) is float)) or (not (type(right) is int or type(right) is float))):
                raise TypeMismatchInExpression(ctx)
            if (type(left) is float or type(right) is float):
                if (ctx.op == "+"):
                    return float(left + right)
                if (ctx.op == "-"):
                    return float(left - right)
                if (ctx.op == "*"):
                    return float(left * right)
            else:
                if (ctx.op == "+"):
                    return int(left + right)
                if (ctx.op == "-"):
                    return int(left - right)
                if (ctx.op == "*"):
                    return int(left * right)
        elif (ctx.op == "/"):
            if ((not (type(left) is int or type(left) is float)) or (not (type(right) is int or type(right) is float))):
                raise TypeMismatchInExpression(ctx)
            return float(left / right)
        elif (ctx.op == "&&" or ctx.op == "||"):
            if (not (type(left) is bool) or (not (type(right) is bool))):
                raise TypeMismatchInExpression(ctx)
            if (ctx.op == "&&"):
                return bool(left and right)
            if (ctx.op == "||"):
                return bool(left or right)
        else:
            # < > == or !=
            if (not(type(left) is type(right))):
                raise TypeMismatchInExpression(ctx)
            if (ctx.op == "<"):
                return left < right
            if (ctx.op == ">"):
                return left > right
            if (ctx.op == "=="):
                return left == right
            if (ctx.op == "!="):
                return not (left == right)

    def visitUnOp(self, ctx: UnOp, o):
        o = []
        val = self.visit(ctx.e, o)

        while (type(val) is (BinOp or UnOp)):
            val = self.visit(val)
        if (ctx.op == "-"):
            # + -  *
            if ((not (type(val) is int or type(val) is float))):
                raise TypeMismatchInExpression(ctx)
            if (type(val) is float):
                if (ctx.op == "-"):
                    return float(val)
            else:
                if (ctx.op == "-"):
                    return int(val)

        if (ctx.op == "!"):
            # + -  *
            if (not (type(val) is bool)):
                raise TypeMismatchInExpression(ctx)

            return bool(not val)

    def visitIntLit(self, ctx: IntLit, o):
        return ctx.val

    def visitFloatLit(self, ctx, o):
        return ctx.val

    def visitBoolLit(self, ctx, o):
        return ctx.val
