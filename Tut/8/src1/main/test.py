class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        return ctx.vardelcs().accept(self)

    def visitVarDecl(self, ctx: VarDecl, o: object): pass

    def visitConstDecl(self, ctx: ConstDecl, o: object): pass

    def visitIntType(self, ctx: IntType, o: object): pass

    def visitFloatType(self, ctx: FloatType, o: object): pass

    def visitIntLit(self, ctx: IntLit, o: object): pass
