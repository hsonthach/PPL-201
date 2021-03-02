from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):

    def visitProgram(self, ctx: BKITParser.ProgramContext):
        # Program([VarDecl(Id(a),IntType)])
        # return 1 + ctx.vardecls().accept(self)
        return Program(ctx.vardecls().accept(self))

    def visitVardecls(self, ctx: BKITParser.VardeclsContext):

        # return 1 + ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecltail(self, ctx: BKITParser.VardecltailContext):
        if (ctx.getChildCount() == 0):
            return []
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecl(self, ctx: BKITParser.VardeclContext):
        # return [VarDecl(ctx.ids().accept(self), ctx.mptype().accept(self))]
        # return list of ids
        return [VarDecl(id, ctx.mptype().accept(self)) for id in ctx.ids().accept(self)]
        # return 1 + ctx.mptype().accept(self) + ctx.ids().accept(self)

    def visitMptype(self, ctx: BKITParser.MptypeContext):
        if (ctx.INTTYPE() != None):
            return IntType()
        return FloatType()

    def visitIds(self, ctx: BKITParser.IdsContext):
        if (ctx.getChildCount() == 1):
            # TODO: return list of ids
            # [a ,b ,c ]
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + ctx.ids().accept(self)
