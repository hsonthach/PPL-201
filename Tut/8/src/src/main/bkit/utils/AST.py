from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from Visitor import Visitor


def printlist(lst, f=str, start="[", sepa=",", ending="]"):
    return start + sepa.join(f(i) for i in lst) + ending


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        return v.visit(self, param)


class Exp(ABC):
    pass


@dataclass
class BinOp(Exp):
    op: str
    e1: Exp
    e2: Exp
    # op is +,-,*,/,&&,||, >, <, ==, or  !=

    def accept(self, v, param):
        return v.visitBinOp(self, param)


@dataclass
class UnOp(Exp):
    op: str
    e: Exp

    def accept(self, v, param):
        return v.visitUnOp(self, param)


@dataclass
class IntLit(Exp):
    val: int

    def accept(self, v, param):
        return v.visitIntLit(self, param)


@dataclass
class FloatLit(Exp):
    val: float

    def accept(self, v, param):
        return v.visitFloatLit(self, param)


@dataclass
class BoolLit(Exp):
    val: bool

    def accept(self, v, param):
        return v.visitBoolLit(self, param)


# @dataclass
# class Program(AST):
#     decl: List[Decl]

#     def accept(self, v, param):
#         return v.visitProgram(self, param)


# @dataclass
# class VarDecl(Decl):
#     name: str
#     typ: Type

#     def accept(self, v, param):
#         return v.visitVarDecl(self, param)


# @dataclass
# class ConstDecl(Decl):
#     name: str
#     val: Lit

#     def accept(self, v, param):
#         return v.visitConstDecl(self, param)


# @dataclass
# class FuncDecl(Decl):
#     name: str
#     param: List[VarDecl]
#     body: Tuple[List[Decl], List[Expr]]

#     def accept(self, v, param):
#         return v.visitFuncDecl(self, param)


# class IntType(Type):
#     pass


# class FloatType(Type):
#     pass


# @dataclass
# class IntLit(Lit):
#     val: int


# @dataclass
# class Id(Expr):
#     name: str

#     def accept(self, v, param):
#         return v.visitId(self, param)
