

# from functools import reduce

class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        o = {
            'parent': [],
            'child': []
        }
        for x in ctx.decl:
            self.visit(x, o)
        pass

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ([*filter(lambda x:ctx.name == x, o["child"])]):
            raise RedeclaredVariable(ctx.name)
        o["child"].append(ctx.name)
        pass

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ([*filter(lambda x:ctx.name == x, o["child"])]):
            raise RedeclaredConstant(ctx.name)
        o["child"].append(ctx.name)
        pass

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        # check only for 1 scope
        if ([*filter(lambda x:ctx.name == x, o["child"])]):
            raise RedeclaredFunction(ctx.name)
        o["child"].append(ctx.name)
        #print("func name", ctx.name)
        #print("Object", o)

        func_o = {
            "parent": o["child"],
            "child": []
        }
        # visit para
        for x in ctx.param:
            self.visit(x, func_o)
        # visit body_decl
        body_decl = ctx.body[0]
        # print(body_decl)
        for x in body_decl:
            self.visit(x, func_o)

        # visit body_expr
        body_expr = ctx.body[1]
        for x in body_expr:
            self.visit(x, o["parent"] + o["child"] + func_o["child"])
        pass

    def visitIntType(self, ctx: IntType, o: object): pass

    def visitFloatType(self, ctx: FloatType, o: object): pass

    def visitIntLit(self, ctx: IntLit, o: object): pass

    def visitId(self, ctx: Id, o: object):
        #print("O", o)
        #print("Current id", ctx.name)
        #print("Undeclared ?", len([x for x in o if (ctx.name == x)]) == 0)
        if (len([x for x in o if (ctx.name == x)]) == 0):
            raise UndeclaredIdentifier(ctx.name)

# numbers = [1, 2, 3, 4]
# print([*filter(lambda x: x == 4, numbers)])


Program([
    VarDecl("b", IntType()),
    FuncDecl(
        "a",
        [VarDecl("m", FloatType()), VarDecl(
            "b", IntType()), VarDecl("d", FloatType())],
        ([ConstDecl("c", IntLit(3)),
          FuncDecl("foo",
                   [VarDecl("x", IntType())],
                   ([VarDecl("y", IntType()), VarDecl("z", IntType())], [
                       Id("y"), Id("x"), Id("foo"), Id("c"), Id("m"), Id("a")])
                   )],
            [Id("foo"), Id("d"), Id("z")])
    )
])
# b,a,
# m,b,d,
# foo,d,z
# c,foo
# y,x,foo,c,m,a # foo,c,m,b,d,a
