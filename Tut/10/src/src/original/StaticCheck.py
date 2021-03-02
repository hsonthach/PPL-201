from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        self.visit(self.ast, None)

    def visitProgram(self, ast: Program, param):
        return None

    def visitVarDecl(self, ast: VarDecl, param):
        return None

    def visitFuncDecl(self, ast: FuncDecl, param):
        return None

    def visitBinaryOp(self, ast: BinaryOp, param):
        return None

    def visitUnaryOp(self, ast: UnaryOp, param):
        return None

    def visitCallExpr(self, ast: CallExpr, param):
        return None

    def visitId(self, ast: Id, param):
        return None

    def visitArrayCell(self, ast: ArrayCell, param):
        return None

    def visitAssign(self, ast: Assign, param):
        return None

    def visitIf(self, ast: If, param):
        return None

    def visitFor(self, ast: For, param):
        return None

    def visitContinue(self, ast: Continue, param):
        return None

    def visitBreak(self, ast: Break, param):
        return None

    def visitReturn(self, ast: Return, param):
        return None

    def visitDowhile(self, ast: Dowhile, param):
        return None

    def visitWhile(self, ast: While, param):
        return None

    def visitCallStmt(self, ast: CallStmt, param):
        return None

    def visitIntLiteral(self, ast: IntLiteral, param):
        return None

    def visitFloatLiteral(self, ast: FloatLiteral, param):
        return None

    def visitBooleanLiteral(self, ast: BooleanLiteral, param):
        return None

    def visitStringLiteral(self, ast: StringLiteral, param):
        return None

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        return None
