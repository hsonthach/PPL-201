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


'''
* Input:
* Precondition: 
* Output: el["typ"] = typ
* Postcondition:
* Description:
* Example:
* Source:
* Exception:
'''


def check_id_type(o, ctx):
    if (ctx["name"] is None):
        return ctx
    for el in o:
        if (el["name"] == ctx["name"]):
            return el


def infer(o, ctx, typ):
    is_exist = False
    for el in o:
        if (el["name"] == ctx["name"]):
            is_exist = True
            el["type"] = typ
    if not (is_exist):
        raise UndeclaredIdentifier(ctx["name"])


class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        self.visit(self.ast, None)

    def visitProgram(self, ctx: Program, o):
        o = []
        decl_list = ctx.decl
        stmt_list = ctx.stmts
        for decl in decl_list:
            self.visit(decl, o)

        for stmt in stmt_list:
            self.visit(stmt, o)

    def visitVarDecl(self, ctx: VarDecl, o):
        o.append({
            "name": ctx.name,
            "type": None
        })

    def visitAssign(self, ctx: Assign, o):
        left = self.visit(ctx.lhs, o)
        right = self.visit(ctx.rhs, o)
        # recursive left & right till it become literals

        # Check TypeMismatchInExpression
        left = check_id_type(o, left)
        right = check_id_type(o, right)

        if (left["type"] is None and right["type"] is None):
            raise TypeCannotBeInferred(ctx)

         # infer
        if left["type"] is None:
            infer(o, left, right["type"])

        if right["type"] is None:
            infer(o, right, left["type"])

        if not (left["type"] is right["type"]):
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self, ctx: BinOp, o):
        left = ctx.e1
        right = ctx.e2
        # recursive left & right till it become literals
        left = check_id_type(o, left)
        right = check_id_type(o, right)
        if (ctx.op in ["+", "-", "*", "/"]):
            # Check TypeMismatchInExpression
            if (not (left["type"] in [int, None])) or (not (right["type"] in [int, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if left["type"] is None:
                infer(o, left, int)
            if (right["type"] is None):
                infer(o, right, int)
            # Output
            return {
                "name": None,
                "type": int
            }
        elif (ctx.op in ["+.", "-.", "*.", "/."]):
            # Check TypeMismatchInExpression
            if (not (left["type"] in [float, None])) or (not (right["type"] in [float, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if left["type"] is None:
                infer(o, left, float)
            if (right["type"] is None):
                infer(o, right, float)
            # Output
            return {
                "name": None,
                "type": float
            }
        elif (ctx.op in [">", "="]):
            # Check TypeMismatchInExpression
            if (not (left["type"] in [int, None])) or (not (right["type"] in [int, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if left["type"] is None:
                infer(o, left, int)
            if (right["type"] is None):
                infer(o, right, int)
            # Output
            return {
                "name": None,
                "type": bool
            }
        elif (ctx.op in [">.", "=."]):
            # Check TypeMismatchInExpression
            if (not (left["type"] in [float, None])) or (not (right["type"] in [float, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if left["type"] is None:
                infer(o, left, float)
            if (right["type"] is None):
                infer(o, right, float)
            # Output
            return {
                "name": None,
                "type": bool
            }
        elif (ctx.op in ["&&", "||", ">b", "=b"]):
            # Check TypeMismatchInExpression
            if (not (left["type"] in [bool, None])) or (not (right["type"] in [bool, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if left["type"] is None:
                infer(o, left, bool)
            if (right["type"] is None):
                infer(o, right, bool)
            # Output
            return {
                "name": None,
                "type": bool
            }

    def visitUnOp(self, ctx: UnOp, o):
        val = ctx.e
        # recursive left & right till it become literals

        val = check_id_type(o, val)

        if (ctx.op in ["i2f"]):
            # Check TypeMismatchInExpression
            if (not (val["type"] in [int, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if val["type"] is None:
                infer(o, val, int)
            # Output
            return {
                "name": None,
                "type": float
            }
        elif (ctx.op in ['-']):
            # Check TypeMismatchInExpression
            if (not (val["type"] in [int, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if val["type"] is None:
                infer(o, val, int)

            # Output
            return {
                "name": None,
                "type": int
            }
        elif (ctx.op in ['-.']):
            # Check TypeMismatchInExpression
            if (not (val["type"] in [float, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if val["type"] is None:
                infer(o, val, float)

            # Output
            return {
                "name": None,
                "type": float
            }
        elif (ctx.op in ["floor"]):
            # Check TypeMismatchInExpression
            if (not (val["type"] in [int, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if val["type"] is None:
                infer(o, val, int)
            # Output
            return {
                "name": None,
                "type": float
            }
        elif (ctx.op in ['!']):
            # Check TypeMismatchInExpression
            if (not (val["type"] in [bool, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if val["type"] is None:
                infer(o, val, bool)
            # Output
            return {
                "name": None,
                "type": bool
            }

    def visitIntLit(self, ctx: IntLit, o):
        return {
            "name": None,
            "type": int
        }

    def visitFloatLit(self, ctx, o):
        return {
            "name": None,
            "type": float
        }

    def visitBoolLit(self, ctx, o):
        return {
            "name": None,
            "type": bool
        }

    def visitId(self, ctx, o):
        if not ([el for el in o if (el["name"] == ctx.name)]):
            raise UndeclaredIdentifier(ctx.name)

        return {
            "name": ctx.name,
            "type": None
        }
