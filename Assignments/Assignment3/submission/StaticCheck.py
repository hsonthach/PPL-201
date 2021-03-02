
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class IntType(Prim):
    pass


class FloatType(Prim):
    pass


class StringType(Prim):
    pass


class BoolType(Prim):
    pass


class VoidType(Type):
    pass


class Unknown(Type):
    pass


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type


@dataclass
class MType:
    intype: List[Type]
    restype: Type


@dataclass
class Symbol:
    name: str
    mtype: Type


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float", MType([FloatType()], IntType())),
            Symbol("float_of_int", MType([IntType()], FloatType())),
            Symbol("int_of_string", MType([StringType()], IntType())),
            Symbol("string_of_int", MType([IntType()], StringType())),
            Symbol("float_of_string", MType([StringType()], FloatType())),
            Symbol("string_of_float", MType([FloatType()], StringType())),
            Symbol("bool_of_string", MType([StringType()], BoolType())),
            Symbol("string_of_bool", MType([BoolType()], StringType())),
            Symbol("read", MType([], StringType())),
            Symbol("printLn", MType([], VoidType())),
            Symbol("printStr", MType([StringType()], VoidType())),
            Symbol("printStrLn", MType([StringType()], VoidType()))
        ]
        self.allowAddVarDecl = False
        self.allowAddFuncDecl = True
        self.ignoreCallFunction = True
        self.noMoreCheckRedeclare = False

    def check(self):
        return self.visit(self.ast, self.global_envi)
    """Declaration"""

    def checkRedeclare(self, env, name, kind):
        if (self.noMoreCheckRedeclare):
            return
        for el in env:
            if (el.name == name):
                raise Redeclared(kind, name)

    def checkEntryPoint(self, env):
        for el in env:
            if (el.name == 'main'):
                return True

        raise NoEntryPoint()

    def get_symbol_by_name(self, name, env):
        for el in env:
            if (el.name == name):
                return el

    def get_type_by_symbol(self, symbol, env):
        if (symbol.name == None):
            return symbol.mtype
        for el in env:
            if (el.name == symbol.name):
                return el.mtype

    def update_env(self, env, name, typ):
        if (name is None):
            return
        for el in env:
            if (el.name == name):
                el.mtype = typ
                break
    '''
    * Input: Tuple[List[VarDecl],List[Stmt]]
    * Precondition:
    * Output:
    * Postcondition:
    * Description: setup env for block and visit vardecl & stmt list
    * Example:
    * Source:
    * Exception:
    '''

    def body_handler(self, tup_of_body, ctx, o, custom_env=None):
        # Setup of env
        env = {
            "non_local": [*o["local"], *o["non_local"]],
            "local": [],
            "parent_ctx": ctx,
            "output_type": o["output_type"]
        } if (custom_env is None) else custom_env
        # visit  vardecl_list and stmt_list
        vardecl_list = list(
            map(lambda x: self.visit(x, env), tup_of_body[0]))
        stmt_list = list(map(lambda x: self.visit(x, env), tup_of_body[1]))

    def is_the_same_array_type(self, arr1, arr2):
        dimen1 = arr1.dimen
        dimen2 = arr2.dimen
        typ1 = arr1.eletype
        typ2 = arr2.eletype
        if (len(dimen1) != len(dimen2)):
            return False
        if (type(typ1) is not type(typ2)):
            return False
        for i, el in enumerate(dimen1):
            if dimen1[i] != dimen2[i]:
                return False

        return True

    def visitProgram(self, ctx, o):
        env = {
            "non_local": [],
            "local": self.global_envi,
            "parent_ctx": ctx
        }
        # Add function symbol, check redeclare function
        for x in ctx.decl:
            self.visit(x, env)

        self.allowAddFuncDecl = False
        self.allowAddVarDecl = True
        self.checkEntryPoint(self.global_envi)
        env["parent_ctx"] = ctx
        # Check vardeclare and function declare
        for x in ctx.decl:
            self.visit(x, env)

        self.ignoreCallFunction = False
        self.noMoreCheckRedeclare = True

        env["parent_ctx"] = ctx
        # Check callexp and call stmt
        for x in ctx.decl:
            self.visit(x, env)

    def visitVarDecl(self, ctx, o):
        if (type(o["parent_ctx"]) is Program and (not self.allowAddVarDecl)) or ((not type(o["parent_ctx"]) is Program) and self.allowAddVarDecl):
            # Second time visit Add name to non_local env, main logic implemented
            # Update ctx
            parent_ctx = o["parent_ctx"]
            #o["parent_ctx"] = ctx
            name = self.visit(ctx.variable, {**o, "parent_ctx": ctx}).name
            dimen = ctx.varDimen

            # Check varinit type is unknown ?
            if (ctx.varInit):
                varInit = self.visit(ctx.varInit, o)
            else:
                varInit = Symbol(None, Unknown())
            if (type(parent_ctx) is Parameter):
                self.checkRedeclare(o["local"], name, Parameter())
            else:
                self.checkRedeclare(o["local"], name, Variable())

            symbol = Symbol(name, varInit.mtype)
            o["local"].append(symbol)
            return symbol
        else:
            pass

    def visitFuncDecl(self, ctx, o):

        #      name: Id
        # param: List[VarDecl]
        # body: Tuple[List[VarDecl],List[Stmt]]
        name = self.visit(ctx.name, {**o, 'parent_ctx': ctx}).name
        if (self.allowAddFuncDecl):
            # First time visit, Add name to global env

            self.checkRedeclare(self.global_envi, name, Function())
            symbol = Symbol(name, MType([], VoidType()))
            self.global_envi.append(symbol)

        else:
            # Check parameter redeclare
            env = {
                "non_local": o["local"],
                "local": [],
                "parent_ctx": ctx,
                "input_type": [],
                "output_type": VoidType()
            }
            # Second time visit,No adding name, main logic implemented, modify param and body
            param_symbol_list = list(map(lambda x: self.visit(
                x, {**env, "parent_ctx": Parameter()}), ctx.param))
            # BODY
            self.body_handler(ctx.body, ctx, o, env)

            #  Modify param and body
            param_type_list = list(
                map(lambda x: self.get_type_by_symbol(x, [*env["local"], *env["non_local"]]), param_symbol_list))

            func_decl_symbol = self.get_symbol_by_name(name, self.global_envi)

            func_decl_symbol.mtype.intype = param_type_list
            func_decl_symbol.mtype.restype = env["output_type"]

    """Expression"""

    def visitArrayCell(self, ctx, o):
        #       arr:Expr
        # idx:List[Expr]
        o["parent_ctx"] = ctx
        exp_symbol = self.visit(
            ctx.arr, o)
        exp_type = self.get_type_by_symbol(
            exp_symbol, [*o["local"], *o["non_local"]])
        idx_list_symbol = list(
            map(lambda x: self.visit(x, o), ctx.idx))
        idx_list_type = list(
            map(lambda x: self.get_type_by_symbol(self.visit(x, o), [*o['local'], *o['non_local']]), ctx.idx))

        if (type(exp_type) in [MType]):
            return Symbol(None, MType(Unknown(), Unknown()))

        # Check lhs type
        if not (type(exp_type) in [ArrayType, Unknown]):
            raise TypeMismatchInExpression(ctx)
        elif (type(exp_type) is ArrayType):
            # Check if dimen of array type and exp is the same
            if (len(exp_type.dimen) != len(idx_list_type)):
                raise TypeMismatchInExpression(ctx)

        # Check value of exp in left type
        for idx_type in idx_list_type:
            if not (type(idx_type) in [Unknown, IntType]):
                raise TypeMismatchInExpression(ctx)

        # Infer rhs
        for i, idx_type in enumerate(idx_list_type):
            if (type(idx_type) is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                idx_list_symbol[i].name, IntType())

        # Infer lhs
        if (type(exp_type) is Unknown):
            self.update_env([*o["local"], *o["non_local"]],
                            exp_symbol.name, ArrayType(idx_list_type, Unknown()))

        return Symbol(None, exp_symbol.mtype.eletype)

    def visitBinaryOp(self, ctx, o):
        #      op:str
        # left:Expr
        # right:Expr
        o["parent_ctx"] = ctx
        left_symbol = self.visit(ctx.left, o)
        left_type = type(self.get_type_by_symbol(
            left_symbol, [*o["local"], *o["non_local"]]))
        right_symbol = self.visit(ctx.right, o)
        right_type = type(self.get_type_by_symbol(
            right_symbol, [*o["local"], *o["non_local"]]))

        if (left_type is MType or right_type is MType):
            return Symbol(None, MType(Unknown(), Unknown()))

        if (ctx.op in ["-", '+', '*', '\\', '%']):
            if not(left_type in [IntType, Unknown]) or not (right_type in [IntType, Unknown]):
                raise TypeMismatchInExpression(ctx)
            if (left_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                left_symbol.name, IntType())

            if (right_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                right_symbol.name, IntType())

            return Symbol(None, IntType())

        elif(ctx.op in ["-.", '+.', '*.', '\\.']):
            if not(left_type in [FloatType, Unknown]) or not (right_type in [FloatType, Unknown]):
                raise TypeMismatchInExpression(ctx)
            if (left_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                left_symbol.name, FloatType())

            if (right_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                right_symbol.name, FloatType())

            return Symbol(None, FloatType())

        elif(ctx.op in ['==', '!=', '<', '>', '<=', ">="]):
            if not(left_type in [IntType, Unknown]) or not (right_type in [IntType, Unknown]):
                raise TypeMismatchInExpression(ctx)
            if (left_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                left_symbol.name, IntType())

            if (right_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                right_symbol.name, IntType())
            return Symbol(None, BoolType())

        elif(ctx.op in ['=/=', '<.', '>.', '<=.', '>=.']):
            if not(left_type in [FloatType, Unknown]) or not (right_type in [FloatType, Unknown]):
                raise TypeMismatchInExpression(ctx)
            if (left_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                left_symbol.name, FloatType())

            if (right_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                right_symbol.name, FloatType())
            return Symbol(None, BoolType())

        elif(ctx.op in ['&&', '||']):
            if not(left_type in [BoolType, Unknown]) or not (right_type in [BoolType, Unknown]):
                raise TypeMismatchInExpression(ctx)
            if (left_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                left_symbol.name, BoolType())

            if (right_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                right_symbol.name, BoolType())
            return Symbol(None, BoolType())

    def visitUnaryOp(self, ctx, o):
        #     op:str -,-.,!
        # body:Expr
        o["parent_ctx"] = ctx
        val_symbol = self.visit(ctx.body, o)

        val_type = type(self.get_type_by_symbol(
            val_symbol, [*o["local"], *o["non_local"]]))

        if (val_type is MType):
            return Symbol(None, MType(Unknown(), Unknown()))
        if (ctx.op in ["-"]):
            if not(val_type in [IntType, Unknown]):
                raise TypeMismatchInExpression(ctx)
            if (val_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                val_symbol.name, IntType())

            return Symbol(None, IntType())

        elif(ctx.op in ["-."]):
            if not(val_type in [FloatType, Unknown]):
                raise TypeMismatchInExpression(ctx)
            if (val_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                val_symbol.name, FloatType())

            return Symbol(None, FloatType())

        elif(ctx.op in ['!']):
            if not(val_type in [BoolType, Unknown]):
                raise TypeMismatchInExpression(ctx)
            if (val_type is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                val_symbol.name, BoolType())
            return Symbol(None, BoolType())

    def visitCallExpr(self, ctx, o):
        o["parent_ctx"] = ctx
        id_symbol = self.visit(ctx.method, o)
        if (self.ignoreCallFunction):
            return Symbol(id_symbol.name, MType(Unknown(), Unknown()))

        exp_mtype_list = list(map(lambda x: self.get_type_by_symbol(
            self.visit(x, o), [*o["local"], *o["non_local"]]), ctx.param))

        func_symbol = self.get_symbol_by_name(
            id_symbol.name, [*o["local"], *o["non_local"]])

        # Check if type is function (Mtype)
        if not (type(func_symbol.mtype) is MType):
            raise TypeMismatchInExpression(ctx)

        # Check input(param length and type)
        if (len(func_symbol.mtype.intype) != len(exp_mtype_list)):
            raise TypeMismatchInExpression(ctx)

        arg_type_list = func_symbol.mtype.intype

        for i, arg in enumerate(arg_type_list):
            # Check infer for input
            if (type(arg) is Unknown):
                raise TypeCannotBeInferred(ctx)

            if not (type(arg) is type(exp_mtype_list[i])):
                raise TypeMismatchInExpression(ctx)

        return Symbol(None, func_symbol.mtype.restype)

    def visitId(self, ctx, o):
        for el in [*o["local"], *o["non_local"]]:
            if (el.name == ctx.name):
                return el
        # No raise error for decl
        if (isinstance(o["parent_ctx"], Decl)):
            return Symbol(ctx.name, Unknown())

        # TODO: uncleare call expr for function and indentifier
        if (type(o["parent_ctx"]) in [CallExpr, CallStmt]):
            raise Undeclared(Function(), ctx.name)

        raise Undeclared(Identifier(), ctx.name)

    """Stmt"""

    def visitAssign(self, ctx, o):
        #      lhs: LHS
        # rhs: Expr
        o["parent_ctx"] = ctx

        lhs_symbol = self.visit(ctx.lhs, o)
        lhs_type = self.get_type_by_symbol(
            lhs_symbol, [*o["local"], *o["non_local"]])
        rhs_symbol = self.visit(ctx.rhs, o)
        rhs_type = self.get_type_by_symbol(
            rhs_symbol, [*o["local"], *o["non_local"]])
        # Handler Mtype
        if (type(lhs_type) is MType or type(rhs_type) is MType):
            return

        # Handler array type
        if (type(lhs_type) is ArrayType and type(rhs_type) is ArrayType):
            if not (self.is_the_same_array_type(lhs_type, rhs_type)):
                raise TypeMismatchInStatement(ctx)

        if (type(lhs_type) is VoidType) or (type(rhs_type) is VoidType):
            raise TypeMismatchInStatement(ctx)
        elif (type(lhs_type) is Unknown and type(rhs_type) is Unknown):
            raise TypeCannotBeInferred(ctx)
        elif (type(lhs_type) is not Unknown and type(rhs_type) is not Unknown):
            if (type(lhs_type) is not type(rhs_type)):
                raise TypeMismatchInStatement(ctx)
        # update env
        if type(lhs_type) is Unknown:
            self.update_env([*o["local"], *o["non_local"]],
                            lhs_symbol.name, rhs_type)

        if type(rhs_type) is Unknown:
            self.update_env([*o["local"], *o["non_local"]],
                            rhs_symbol.name, lhs_type)

    def visitIf(self, ctx, o):
        #      ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
        o["parent_ctx"] = ctx

        def if_then_handler(tup_of_if):
            # Check exp and infer
            exp_symbol = self.visit(tup_of_if[0], o)
            exp_mtype = self.get_type_by_symbol(
                exp_symbol, [*o["local"], *o["non_local"]])
            if (type(exp_mtype) is MType):
                return
            if not(type(exp_mtype) in [BoolType, Unknown]):
                raise TypeMismatchInStatement(ctx)

            if (type(exp_mtype) is Unknown):
                self.update_env([*o["local"], *o["non_local"]],
                                exp_symbol.name, BoolType())

            self.body_handler((tup_of_if[1], tup_of_if[2]), ctx, o)

        for if_then_ctx in ctx.ifthenStmt:
            if_then_handler(if_then_ctx)

        self.body_handler(ctx.elseStmt, ctx, o)

    def visitFor(self, ctx, o):
        # idx1: Id
        # expr1:Expr
        # expr2:Expr
        # expr3:Expr
        # loop: Tuple[List[VarDecl],List[Stmt]]
        o["parent_ctx"] = ctx

        id = self.visit(ctx.idx1, o)
        expr1_symbol = self.visit(ctx.expr1, o)
        expr1_mtype = self.get_type_by_symbol(
            expr1_symbol, [*o["local"], *o["non_local"]])
        expr2_symbol = self.visit(ctx.expr2, o)
        expr2_mtype = self.get_type_by_symbol(
            expr2_symbol, [*o["local"], *o["non_local"]])
        expr3_symbol = self.visit(ctx.expr3, o)
        expr3_mtype = self.get_type_by_symbol(
            expr3_symbol, [*o["local"], *o["non_local"]])
        if (type(expr1_mtype) is MType):
            return
        if (type(expr2_mtype) is MType):
            return
        if (type(expr2_mtype) is MType):
            return

        if not(type(expr1_mtype) in [IntType, Unknown]) or not(type(expr3_mtype) in [IntType, Unknown]):
            raise TypeMismatchInStatement(ctx)
        if not(type(expr2_mtype) in [BoolType, Unknown]):
            raise TypeMismatchInStatement(ctx)

        if (type(expr1_mtype) is Unknown):
            self.update_env([*o["local"], *o["non_local"]],
                            expr1_symbol.name, IntType())
        if (type(expr2_mtype) is Unknown):
            self.update_env([*o["local"], *o["non_local"]],
                            expr3_symbol.name, IntType())
        if (type(expr3_mtype) is Unknown):
            self.update_env([*o["local"], *o["non_local"]],
                            expr2_symbol.name, BoolType())

        self.body_handler(ctx.loop, ctx, o)

    def visitBreak(self, ctx, o):
        pass

    def visitContinue(self, ctx, o):
        pass

    def visitReturn(self, ctx, o):
        # expr:Expr # None if no expression
        o["parent_ctx"] = ctx
        if (ctx.expr is None):
            o["output_type"] = VoidType()
            return

        expr_symbol = self.visit(ctx.expr, o)
        expr_mtype = self.get_type_by_symbol(
            expr_symbol, [*o["local"], *o["non_local"]])

        if (type(expr_mtype) is MType):
            o["output_type"] = expr_mtype.restype
            return

        o["output_type"] = self.get_type_by_symbol(
            expr_symbol, [*o["local"], *o["non_local"]])

    def visitDowhile(self, ctx, o):
        o['parent_ctx'] = ctx
        exp_symbol = self.visit(ctx.exp, o)
        exp_mtype = self.get_type_by_symbol(
            exp_symbol, [*o["local"], *o["non_local"]])

        if (type(exp_mtype) is MType):
            return

        if not(type(exp_mtype) in [BoolType, Unknown]):
            raise TypeMismatchInStatement(ctx)
        if (type(exp_mtype) is Unknown):
            self.update_env([*o["local"], *o["non_local"]],
                            exp_symbol.name, BoolType())

        self.body_handler(ctx.sl, ctx, o)

    def visitWhile(self, ctx, o):
        # exp: Expr
        # sl:Tuple[List[VarDecl],List[Stmt]]
        o['parent_ctx'] = ctx
        exp_symbol = self.visit(ctx.exp, o)

        exp_mtype = self.get_type_by_symbol(
            exp_symbol, [*o["local"], *o["non_local"]])
        if (type(exp_mtype) is MType):
            return
        if not(type(exp_mtype) in [BoolType, Unknown]):
            raise TypeMismatchInStatement(ctx)
        if (type(exp_mtype) is Unknown):
            self.update_env([*o["local"], *o["non_local"]],
                            exp_symbol.name, BoolType())

        self.body_handler(ctx.sl, ctx, o)

    def visitCallStmt(self, ctx, o):
        #     method:Id
        # param:List[Expr]
        if (self.ignoreCallFunction):
            return

        o["parent_ctx"] = ctx
        id_symbol = self.visit(ctx.method, o)
        exp_mtype_list = list(map(lambda x: self.get_type_by_symbol(
            self.visit(x, o), [*o["local"], *o["non_local"]]), ctx.param))

        func_symbol = self.get_symbol_by_name(
            id_symbol.name, [*o["local"], *o["non_local"]])

        arg_type_list = func_symbol.mtype.intype

        # Check if type is function (Mtype)
        if not (type(func_symbol.mtype) is MType):
            raise TypeMismatchInStatement(ctx)

        # Check if output is VoidType
        if not (type(func_symbol.mtype.restype) is VoidType):
            raise TypeMismatchInStatement(ctx)

        # Check input
        if (len(func_symbol.mtype.intype) != len(exp_mtype_list)):
            raise TypeMismatchInStatement(ctx)
        for i, arg in enumerate(arg_type_list):
            # Check infer for input
            if (type(arg) is Unknown):
                raise TypeCannotBeInferred(ctx)

            if not (type(arg) is type(exp_mtype_list[i])):
                raise TypeMismatchInStatement(ctx)

    """Literal"""

    def visitIntLiteral(self, ctx, o):
        return Symbol(None, IntType())

    def visitFloatLiteral(self, ctx, o):
        return Symbol(None, FloatType())

    def visitStringLiteral(self, ctx, o):
        return Symbol(None, StringType())

    def visitBooleanLiteral(self, ctx, o):
        return Symbol(None, BoolType())

    def visitArrayLiteral(self, ctx, o):
        # value:List[Literal]
        literal_types = list(
            map(lambda x: self.get_type_by_symbol(self.visit(x, o), [*o['local'], *o['non_local']]), ctx.value))
        # Array of array
        if (type(literal_types[0]) is ArrayType):
            # Get dimension of child array
            dimen = literal_types[0].dimen
            # Get literal type
            return Symbol(None, ArrayType([len(literal_types)] + dimen, literal_types[0].eletype))

        return Symbol(None, ArrayType([len(literal_types)], literal_types[0]))
