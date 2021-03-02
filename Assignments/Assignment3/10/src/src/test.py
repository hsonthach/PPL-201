

from functools import reduce


class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        o = []
        for x in ctx.decl:
            self.visit(x, o)
            o += x.name

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if (ctx.name in o):
            raise RedeclaredVariable(ctx.name)

        return ctx

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if (ctx.name in o):
            raise RedeclaredConstant(ctx.name)

        return ctx

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        # check only for 1 scope
        if (ctx.name in o):
            raise RedeclaredFunction(ctx.name)

        func_o = []
        # visit para
        for x in ctx.para:
            self.visit(x, func_o)
            func_o += x.name
        # visit body
        for x in ctx.body:
            self.visit(x, func_o)
            func_o += x.name
        return ctx

    def visitIntType(self, ctx: IntType, o: object): pass

    def visitFloatType(self, ctx: FloatType, o: object): pass

    def visitIntLit(self, ctx: IntLit, o: object): pass
