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


class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        self.visit(self.ast, None)

    def visitProgram(self, ctx: Program, o):
        decl_list = ctx.decl
        stmt_list = ctx.stmts
        o = {
            'non_local': [],
            'local': []
        }
        for decl in decl_list:

    def visitVarDecl(self, ctx: VarDecl, o): pass

    def visitFuncDecl(self, ctx: FuncDecl, o): pass

    def visitCallStmt(self, ctx: CallStmt, o): pass

    def visitAssign(self, ctx: Assign, o): pass

    def visitIntLit(self, ctx: IntLit, o): pass

    def visitFloatLit(self, ctx, o): pass

    def visitBoolLit(self, ctx, o): pass

    def visitId(self, ctx, o): pass
