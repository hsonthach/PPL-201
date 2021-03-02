from prog3header import *
from functools import reduce

"""
NOTE: 
    [+ , - , *, /]      : int -> int
    [+., -., *., /.]    : float -> float
    [>, =]              : int -> bool
    [>., =.]            : float -> bool
    [!, &&, ||, >b, =b] : bool -> bool
    [i2f]               : int -> float
    [floor]             : float -> int

    ASSIGN stmt : type(lhs) == type(rhs)
    or else     : raise TypeMismatchInStatement(ctx)

    Inferring type:
    |   Id not in declarations,
    |   raise UndeclaredIdentifier(ctx)
    or
    |   Id cannot be inferred in the first usage,
    |   raise TypeCannotBeInferred(ctx)
        



"""


class UnreferredType(Type):
    def accept(self, v, o):
        return v.visitFloatType(self, o)

    def __str__(self):
        return "UnreferredType()"


class VarType:
    def __init__(self, n: str, t: Type):
        self.name = n
        self.typ = t

    def __str__(self):
        return "VarType(\"" + ('NoName' if not self.name else self.name) + "\"," + str(self.typ) + ")"

    pass


class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        o = reduce(lambda env, i_ctx: env +
                   [self.visit(i_ctx, env)], ctx.decl, [])

        # map(lambda e: self.visit(e, o), ctx.stmts)
        # use for for easier debug :|
        for stmt in ctx.stmts:
            self.visit(stmt, o)
        pass

    def visitVarDecl(self, ctx: VarDecl, o):
        return VarType(ctx.name, UnreferredType())
        pass

    def visitAssign(self, ctx: Assign, o):
        rhs_type = self.visit(ctx.rhs, o)
        lhs_type = self.visit(ctx.lhs, o)

        if type(lhs_type) is type(rhs_type) is UnreferredType:
            raise TypeCannotBeInferred(ctx)
        elif type(lhs_type) is UnreferredType:
            ctx.lhs.accept(self, [VarType(None, rhs_type)] + o)
        # How can this happen?
        elif type(rhs_type) is UnreferredType:
            ctx.rhs.accept(self, [VarType(None, lhs_type)] + o)
        elif type(lhs_type) is not type(rhs_type):
            raise TypeMismatchInStatement(ctx)

        print(ctx)
        [print(e) for e in o]
        print('________________\n')

        pass

    def visitBinOp(self, ctx: BinOp, o):

        l_type = ctx.e1.accept(self, o)
        r_type = ctx.e2.accept(self, o)
        result = UnreferredType()

        def lazy(ltype, rtype, allow_types, type_fix):
            """
            Lazy take ltype, rtype,
            Only work if two operands are same type.
            allow_types is list of allow type,
                for example, op `+` required IntType,
                so allow_types should be [IntType, UnreferredType]
            type_fix is the type that operand should have.

            """
            if type(ltype) not in allow_types \
                    or type(rtype) not in allow_types:
                raise TypeMismatchInExpression(ctx)
            else:
                if type(ltype) is type(rtype) is UnreferredType:
                    ctx.e1.accept(self, [VarType(None, type_fix)] + o)
                    ctx.e2.accept(self, [VarType(None, type_fix)] + o)

                elif type(ltype) is UnreferredType:
                    ctx.e1.accept(self, [VarType(None, type_fix)] + o)

                elif type(r_type) is UnreferredType:
                    ctx.e2.accept(self, [VarType(None, type_fix)] + o)

                else:
                    pass

            pass

        "Work first, optimise later"
        if ctx.op in ['+', '-', '*', '/']:
            lazy(l_type, r_type, [IntType, UnreferredType], IntType())
            result = IntType()

        #
        if ctx.op in ['+.', '-.', '*.', '/.']:
            lazy(l_type, r_type, [FloatType, UnreferredType], FloatType())
            result = FloatType()

        if ctx.op in ['&&', '||', '>b', '=b']:
            lazy(l_type, r_type, [BoolType, UnreferredType], BoolType())
            result = BoolType()

        if ctx.op in ['>', '=']:
            lazy(l_type, r_type, [IntType, UnreferredType], IntType())
            result = BoolType()

        if ctx.op in ['>.', '=.']:
            lazy(l_type, r_type, [FloatType, UnreferredType], FloatType())
            result = BoolType()

        return result
        pass

    def visitUnOp(self, ctx: UnOp, o):

        def lazy(etype, allow_types, type_fix):
            if type(etype) not in allow_types:
                raise TypeMismatchInExpression(ctx)
            else:
                if type(expr_type) is UnreferredType:
                    ctx.e.accept(self, [VarType(None, type_fix)] + o)
                else:
                    pass
            pass

        expr_type = self.visit(ctx.e, o)
        result = UnreferredType()

        if ctx.op == '-':
            lazy(expr_type, [IntType, UnreferredType], IntType())
            result = IntType()

        if ctx.op == '-.':
            lazy(expr_type, [FloatType, UnreferredType], FloatType())
            result = FloatType()

        elif ctx.op == '!':
            lazy(expr_type, [BoolType, UnreferredType], BoolType())
            result = BoolType()

        elif ctx.op == 'i2f':
            lazy(expr_type, [IntType, UnreferredType], IntType())
            result = FloatType()

        elif ctx.op == 'float':
            lazy(expr_type, [IntType, UnreferredType], FloatType())
            result = IntType()

        return result

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()
        pass

    def visitFloatLit(self, ctx, o):
        return FloatType()
        pass

    def visitBoolLit(self, ctx, o):
        return BoolType()
        pass

    def visitId(self, ctx, o):
        set_flag = False
        if o and (o[0].name is None):
            set_flag = True
        for e in o:
            if e.name == ctx.name:
                # TODO: Do something, return something
                if set_flag:
                    e.typ = o[0].typ
                return e.typ
                pass

        raise UndeclaredIdentifier(ctx.name)
        pass


check = StaticCheck()

i = IntLit(None)
f = FloatLit(None)
bo = BoolLit(None)
a = Id('a')
b = Id('b')
c = Id('c')
# ast = Program([VarDecl("x"), VarDecl("y")],
#               [BinOp('+.', BinOp("-.", Id("x"), FloatLit(0.0)), BinOp("*.", Id("y"), FloatLit(0.0)))])

ast = Program([VarDecl("x"), VarDecl("y"), VarDecl("z"), VarDecl('k'), VarDecl('l'), VarDecl('m')],
              [Assign(Id("x"), BinOp(">b", BinOp("&&", Id("x"), Id("y")),
                                     BinOp("||", BoolLit(False),
                                           BinOp(">", Id("z"),
                                                 IntLit(3))))),
               Assign(Id("z"), Id("k")), Assign(Id('m'), UnOp('-.', Id('m')))])
try:
    print(check.visit(ast, None))
except StaticError as ex:
    print(ex)
