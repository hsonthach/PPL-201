
from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce


def flatten_list(lst):
    return reduce(lambda a, b: a + b, lst, [])


class ASTGeneration(BKITVisitor):

    def visitProgram(self, ctx: BKITParser.ProgramContext):
        # return Program(reduce(lambda a, b: a + b.accept(self), ctx.vardecl(), []))
        vardecl_list = list(map(lambda x: x.accept(self), ctx.vardecl()))
        return Program(flatten_list(vardecl_list))

    def visitVardecl(self, ctx: BKITParser.VardeclContext):
        mptype = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        vardecl_list = list(map(lambda id: VarDecl(id, mptype), ids))
        return vardecl_list

    def visitMptype(self, ctx: BKITParser.MptypeContext):
        if (ctx.INTTYPE()):
            return IntType()
        return FloatType()

    def visitIds(self, ctx: BKITParser.IdsContext):
        return list(map(lambda id: Id(id.getText()), ctx.ID()))
