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


def get_type_by_name(o, ctx):
    if (ctx["name"] is None):
        return ctx
    env = [*o["local"], *o["non_local"]]
    for el in env:
        if (el["name"] == ctx["name"]):
            return el


def updateEnv(o, ctx, typ, context=None):
    is_exist = False
    for el in [*o["local"], *o["non_local"]]:
        if (el["name"] == ctx["name"]):
            is_exist = True
            el["type"] = typ
            break


class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        self.visit(self.ast, None)

    def visitProgram(self, ctx: Program, o):
        env = {
            "non_local": [],
            "local": []
        }
        decl_list = ctx.decl
        stmt_list = ctx.stmts

        for decl in decl_list:
            self.visit(decl, env)

        for stmt in stmt_list:
            self.visit(stmt, env)

    def visitVarDecl(self, ctx: VarDecl, o):
        for el in o["local"]:
            if (el["name"] == ctx.name):
                raise Redeclared(ctx)
        vardecl = {
            "name": ctx.name,
            "type": None
        }

        o["local"].append(vardecl)

        return vardecl

    def visitFuncDecl(self, ctx: FuncDecl, o):
        # Check func
        for el in o["local"]:
            if (el["name"] == ctx.name):
                raise Redeclared(ctx)

        env = {
            "non_local": [*o["local"], *o["non_local"]],
            "local": []
        }
        # Update parent env
        param_list = list(map(lambda x: self.visit(x, env), ctx.param))
        o["local"].append({
            "name": ctx.name,
            "type": 'function',
            "param": param_list
        })

        local_list = list(map(lambda x: self.visit(x, env), ctx.local))
        stmt_list = list(map(lambda x: self.visit(x, env), ctx.stmts))  # None

    def visitCallStmt(self, ctx: CallStmt, o):
        # Check undeclare
        isExist = False
        foundFuncDecl = None
        for el in [*o["local"], *o["non_local"]]:
            if (el["name"] == ctx.name and el["type"] == 'function'):
                isExist = True
                foundFuncDecl = el
                break
        if (not isExist):
            raise UndeclaredIdentifier(ctx.name)

        # Check param length
        if (len(foundFuncDecl["param"]) != len(ctx.args)):
            raise TypeMismatchInStatement(ctx)

        # Check type and infer
        for i, param_child in enumerate(foundFuncDecl["param"]):
            arg = self.visit(ctx.args[i], o)

            if (param_child["type"] is None and arg['type'] is None):
                raise TypeCannotBeInferred(ctx)
            elif (param_child["type"] is not None and arg["type"] is not None):
                if not (param_child["type"] is arg["type"]):
                    raise TypeMismatchInStatement(ctx)

            if param_child["type"] is None:
                # update type for func param
                foundFuncDecl['param'][i]["type"] = arg["type"]

            if arg["type"] is None:
                # update type for func param
                arg['type'] = param_child['type']

    def visitAssign(self, ctx: Assign, o):
        left = self.visit(ctx.lhs, o)
        right = self.visit(ctx.rhs, o)

        left = get_type_by_name(o, left)
        right = get_type_by_name(o, right)

        if (left["type"] is None and right["type"] is None):
            raise TypeCannotBeInferred(ctx)

        elif (left["type"] is not None and right["type"] is not None):
            if not (left["type"] is right["type"]):
                raise TypeMismatchInStatement(ctx)
        # update env
        if left["type"] is None:
            updateEnv(o, left, right["type"], ctx)

        if right["type"] is None:
            updateEnv(o, right, left["type"], ctx)
        # TODO
        # update param
        # updateParam(o,)

    def visitBinOp(self, ctx: BinOp, o):
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)

        # recursive left & right till it become literals
        left = get_type_by_name(o, left)
        right = get_type_by_name(o, right)
        if (ctx.op in ["+", "-", "*", "/"]):
            # Check TypeMismatchInExpression
            if (not (left["type"] in [int, None])) or (not (right["type"] in [int, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if left["type"] is None:
                updateEnv(o, left, int)
            if (right["type"] is None):
                updateEnv(o, right, int)
            # Output
            return {
                "name": None,
                "type": int
            }
        elif (ctx.op in ["+.", "-.", "*.", "/."]):
            if (not (left["type"] in [float, None])) or (not (right["type"] in [float, None])):

                raise TypeMismatchInExpression(ctx)

            # infer
            if left["type"] is None:
                updateEnv(o, left, float)
            if (right["type"] is None):
                updateEnv(o, right, float)
            # Output
            return {
                "name": None,
                "type": float
            }
        elif (ctx.op in [">", "="]):
            if (not (left["type"] in [int, None])) or (not (right["type"] in [int, None])):

                raise TypeMismatchInExpression(ctx)

            # infer
            if left["type"] is None:
                updateEnv(o, left, int)
            if (right["type"] is None):
                updateEnv(o, right, int)
            # Output
            return {
                "name": None,
                "type": bool
            }
        elif (ctx.op in [">.", "=."]):
            if (not (left["type"] in [float, None])) or (not (right["type"] in [float, None])):
                raise TypeMismatchInExpression(ctx)

            # infer
            if left["type"] is None:
                updateEnv(o, left, float)
            if (right["type"] is None):
                updateEnv(o, right, float)
            # Output
            return {
                "name": None,
                "type": bool
            }
        elif (ctx.op in ["&&", "||", ">b", "=b"]):
            if (not (left["type"] in [bool, None])) or (not (right["type"] in [bool, None])):

                raise TypeMismatchInExpression(ctx)

            # infer
            if left["type"] is None:
                updateEnv(o, left, bool)
            if (right["type"] is None):
                updateEnv(o, right, bool)
            # Output
            return {
                "name": None,
                "type": bool
            }

    def visitUnOp(self, ctx: UnOp, o):
        val = self.visit(ctx.e, o)
        # recursive left & right till it become literals

        val = get_type_by_name(o, val)

        if (ctx.op in ["i2f"]):
            if (not (val["type"] in [int, None])):

                raise TypeMismatchInExpression(ctx)

            # infer
            if val["type"] is None:
                updateEnv(o, val, int)
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
                updateEnv(o, val, int)

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
                updateEnv(o, val, float)

            # Output
            return {
                "name": None,
                "type": float
            }
        elif (ctx.op in ["floor"]):
            # Check TypeMismatchInExpression
            if (not (val["type"] in [float, None])):

                raise TypeMismatchInExpression(ctx)

            # infer
            if val["type"] is None:
                updateEnv(o, val, float)
            # Output
            return {
                "name": None,
                "type": int
            }
        elif (ctx.op in ['!']):
            # Check TypeMismatchInExpression
            if (not (val["type"] in [bool, None])):

                raise TypeMismatchInExpression(ctx)

            # infer
            if val["type"] is None:
                updateEnv(o, val, bool)
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
        for el in [*o["local"], *o["non_local"]]:
            if (el["name"] == ctx.name):
                return el
        raise UndeclaredIdentifier(ctx.name)
