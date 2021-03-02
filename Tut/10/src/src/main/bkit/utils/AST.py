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
class Program:
    decl: List[Decl]
    stmts: List[Stmt]


@dataclass
class VarDecl(Decl):
    name: str


@dataclass
class FuncDecl(Decl):
    name: str
    param: List[VarDecl]
    local: List[Decl]
    stmts: List[Stmt]


@dataclass
class Assign(Stmt):
    lhs: Id
    rhs: Exp


@dataclass
class CallStmt(Stmt):
    name: str
    args: List[Exp]


@dataclass
class IntLit(Exp):
    val: int


@dataclass
class FloatLit(Exp):
    val: float


@dataclass
class BoolLit(Exp):
    val: bool


@dataclass
class Id(Exp):
    name: str
