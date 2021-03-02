from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce


class ASTGeneration(BKITVisitor):

    def visitProgram(self, ctx: BKITParser.ProgramContext):
        return Program(reduce(lambda a, b: a + b.accept(self), ctx.vardecl(), []))

    def visitVardecl(self, ctx: BKITParser.VardeclContext):
        # [Id(a),Id(b)] # [Id(a)]
        ids = ctx.ids().accept(self)

        return list(map(lambda id: (VarDecl(id, ctx.mptype().accept(self))), ids))

    def visitMptype(self, ctx: BKITParser.MptypeContext):
        if (ctx.INTTYPE() != None):
            return IntType()
        return FloatType()

    def visitIds(self, ctx: BKITParser.IdsContext):
        # ID (',' ID)*
        # [Id(a),Id(b)] # [Id(a)]
        return list(map(lambda ID: Id(ID.getText()), ctx.ID()))
