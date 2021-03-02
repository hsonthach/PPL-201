from abc import ABC
from dataclasses import dataclass
import AST


class StaticError(Exception):
    pass


@dataclass
class RedeclaredVariable(StaticError):

    name: str

    def __str__(self):
        return "RedeclaredVariable " + self.name


@dataclass
class RedeclaredConstant(StaticError):

    name: str

    def __str__(self):
        return "RedeclaredConstant " + self.name


@dataclass
class RedeclaredFunction(StaticError):

    name: str

    def __str__(self):
        return "RedeclaredFunction " + self.name


@dataclass
class UndeclaredIdentifier(StaticError):

    name: str

    def __str__(self):
        return "UndeclaredIdentifier " + self.name


class TypeMismatchInExpression(StaticError):

    def __str__(self):
        return "TypeMismatchInExpression "


class TypeMismatchInStatement(StaticError):

    def __str__(self):
        return "TypeMismatchInStatement "


class TypeCannotBeInferred(StaticError):

    def __str__(self):
        return "TypeCannotBeInferred "
