class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        arr = [{}]
        for x in ctx.decl:
            self.visit(x, arr)
        for x in ctx.stmts:
            self.visit(x, arr)

    def visitVarDecl(self, ctx: VarDecl, o):
        if ctx.name in o[-1]:
            raise Redeclared(ctx)
        o[-1][ctx.name] = None

    def visitBlock(self, ctx: Block, o):
        arr = [{}]
        for x in ctx.decl:
            self.visit(x, arr)
        o += arr
        for x in ctx.stmts:
            self.visit(x, o)
        o.pop(len(o) - 1)
        return ctx

    def visitAssign(self, ctx: Assign, o):
        rhs = self.visit(ctx.rhs, o)
        lhs = self.visit(ctx.lhs, o)

        if (lhs[1] == rhs[1]) and (lhs[1] != None):
            return ctx
        elif (lhs[1] == rhs[1]) and (lhs[1] == None):
            raise TypeCannotBeInferred(ctx)
        elif (lhs[1] == None) and (rhs[1] != None):
            o[lhs[2]][lhs[0]] = rhs[1]
            return ctx
        elif (rhs[1] == None) and (lhs[1] != None):
            o[rhs[2]][rhs[0]] = lhs[1]
            return ctx
        raise TypeMismatchInStatement(ctx)

    def visitBinOp(self, ctx: BinOp, o):
        op = ctx.op
        e1type = self.visit(ctx.e1, o)
        e2type = self.visit(ctx.e2, o)
        if op in ['+', '-', '*', '/']:
            if e1type[1] in ['int', None] and e2type[1] in ['int', None]:
                o[e1type[2]][e1type[0]] = 'int'
                o[e2type[2]][e2type[0]] = 'int'
                return ['', 'int', 0]
            raise TypeMismatchInExpression(ctx)
        elif op in ['+.', '-.', '*.', '/.']:
            if e1type[1] in ['float', None] and e2type[1] in ['float', None]:
                o[e1type[2]][e1type[0]] = 'float'
                o[e2type[2]][e2type[0]] = 'float'
                return ['', 'float', 0]
            raise TypeMismatchInExpression(ctx)
        elif op in ['>', '=']:
            if e1type[1] in ['int', None] and e2type[1] in ['int', None]:
                o[e1type[2]][e1type[0]] = 'int'
                o[e2type[2]][e2type[0]] = 'int'
                return ['', 'bool', 0]
            raise TypeMismatchInExpression(ctx)
        elif op in ['>.', '=.']:
            if e1type[1] in ['float', None] and e2type[1] in ['float', None]:
                o[e1type[2]][e1type[0]] = 'float'
                o[e2type[2]][e2type[0]] = 'float'
                return ['', 'bool', 0]
            raise TypeMismatchInExpression(ctx)
        elif op in ['&&', '||', '>b', '=b']:
            if e1type[1] in ['bool', None] and e2type[1] in ['bool', None]:
                o[e1type[2]][e1type[0]] = 'bool'
                o[e2type[2]][e2type[0]] = 'bool'
                return ['', 'bool', 0]
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx: UnOp, o):
        op = ctx.op
        etype = self.visit(ctx.e, o)
        if op in ['-']:
            if etype[1] == 'int':
                return ['', 'int', 0]
            elif etype[1] == None:
                o[etype[2]][etype[0]] = 'int'
                return ['', 'int', 0]
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['-.']:
            if etype[1] == 'float':
                return ['', 'float', 0]
            elif etype[1] == None:
                o[etype[2]][etype[0]] = 'float'
                return ['', 'float', 0]
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['!']:
            if etype[1] == 'bool':
                return ['', 'bool', 0]
            elif etype[1] == None:
                o[etype[2]][etype[0]] = 'bool'
                return ['', 'bool', 0]
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['i2f']:
            if etype[1] == 'int':
                return ['', 'float', 0]
            elif etype[1] == None:
                o[etype[2]][etype[0]] = 'int'
                return ['', 'float', 0]
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['floor']:
            if etype[1] == 'float':
                return ['', 'int', 0]
            elif etype[1] == None:
                o[etype[2]][etype[0]] = 'float'
                return ['', 'int', 0]
            else:
                raise TypeMismatchInExpression(ctx)

    def visitIntLit(self, ctx: IntLit, o):
        return ['', 'int', 0]

    def visitFloatLit(self, ctx, o):
        return ['', 'float', 0]

    def visitBoolLit(self, ctx, o):
        return ['', 'bool', 0]

    def visitId(self, ctx, o):  # return list of name, type, index of dict
        finddict = [x for x in o if ctx.name in x]
        if finddict:
            return [ctx.name, finddict[-1][ctx.name], o.index(finddict[-1])]
        raise UndeclaredIdentifier(ctx.name)
