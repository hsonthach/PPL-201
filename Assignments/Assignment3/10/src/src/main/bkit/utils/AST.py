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


class Type(ABC):
    pass


class IntType(Type):
    pass


class FloatType(Type):
    pass


class BoolType(Type):
    pass


class Exp(ABC):
    pass


class Stmt(ABC):
    pass


class Decl(ABC):
    pass


@dataclass
class VarDecl(Decl):
    name: str

    def accept(self, v, param):
        return v.visitVarDecl(self, param)


@dataclass
class Id(Exp):
    name: str

    def accept(self, v, param):
        return v.visitId(self, param)


@dataclass
class Assign(Stmt):
    lhs: Id
    rhs: Exp

    def accept(self, v, param):
        return v.visitAssign(self, param)


@dataclass
class Program:
    decl: List[VarDecl]
    stmts: List[Stmt]

    def accept(self, v, param):
        return v.visitProgram(self, param)


@dataclass
class FuncDecl(Decl):
    name: str
    param: List[VarDecl]
    local: List[Decl]
    stmts: List[Stmt]

    def accept(self, v, param):
        return v.visitFuncDecl(self, param)


@dataclass
class BinOp(Exp):
    op: str
    e1: Exp
    e2: Exp  # op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b

    def accept(self, v, param):
        return v.visitBinOp(self, param)


@dataclass
class UnOp(Exp):
    op: str
    e: Exp  # op is -,-., !,i2f, floor

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


@dataclass
class CallStmt(Stmt):
    name: str
    args: List[Exp]

    def accept(self, v, param):
        return v.visitCallStmt(self, param)
