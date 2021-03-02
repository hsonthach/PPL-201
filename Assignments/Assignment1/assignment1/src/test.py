

class Exp(ABC):  # abstract class


class BinOp(Exp):  # op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=


class UnOp(Exp):  # op:str,e:Exp #op is -, !


class IntLit(Exp):  # val:int


class FloatLit(Exp):  # val:float


class BoolLit(Exp):  # val:bool


class StaticCheck(Visitor):

    def visitBinOp(self, ctx: BinOp, o):
        o = []
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)

        while (type(left) is (BinOp or UnOp)):
            left = self.visit(left)
        while (type(right) is (BinOp or UnOp)):
            right = self.visit(right)

        leftType = left["type"]
        leftVal = left["val"]
        rightType = right["type"]
        rightVal = right["val"]

        if (ctx.op == "+" or ctx.op == "-" or ctx.op == "*"):
            # Check input
            allowedInput = ["int", "float"]
            if (not (leftType in allowedInput) or not (leftType in allowedInput)):
                raise TypeMismatchInExpression(ctx)

            # Check output
            if (leftType is "float" or rightType is "float"):
                if (ctx.op == "+"):
                    return float(left + right)
                if (ctx.op == "-"):
                    return float(left - right)
                if (ctx.op == "*"):
                    return float(left * right)
            else:
                if (ctx.op == "+"):
                    return int(left + right)
                if (ctx.op == "-"):
                    return int(left - right)
                if (ctx.op == "*"):
                    return int(left * right)

        elif (ctx.op == "/"):
            allowedInput = ["int", "float"]
            if (not (leftType in allowedInput) or not (rightType in allowedInput)):
                raise TypeMismatchInExpression(ctx)

            return float(left / right)
        elif (ctx.op == "&&" or ctx.op == "||"):
            allowedInput = ["bool"]
            if (not (leftType in allowedInput) or not (rightType in allowedInput)):
                raise TypeMismatchInExpression(ctx)
            if (not (leftType in allowedInput) or not (rightType in allowedInput)):
                raise TypeMismatchInExpression(ctx)
            if (ctx.op == "&&"):
                return bool(left and right)
            if (ctx.op == "||"):
                return bool(left or right)
        else:
            # < > == or !=
            if (leftType == rightType):
                raise TypeMismatchInExpression(ctx)
            if (ctx.op == "<"):
                return left < right
            if (ctx.op == ">"):
                return left > right
            if (ctx.op == "=="):
                return left == right
            if (ctx.op == "!="):
                return not (left == right)

    def visitUnOp(self, ctx: UnOp, o):
        o = []
        val = self.visit(ctx.e, o)

        while (type(val) is (BinOp or UnOp)):
            val = self.visit(val)
        val = val["val"]
        valType = val["type"]

        if (ctx.op == "-"):
            # + -  *
            allowedInput = ["int", "float"]
            if (not (leftType in allowedInput) or not (rightType in allowedInput)):
                raise TypeMismatchInExpression(ctx)

            if (valType == "float"):
                if (ctx.op == "-"):
                    return float(val)
            else:
                if (ctx.op == "-"):
                    return int(val)

        if (ctx.op == "!"):
            # + -  *
            allowedInput = ["bool"]
            if (not (valType in allowedInput)):
                raise TypeMismatchInExpression(ctx)

            return bool(not val)

    def visitIntLit(self, ctx: IntLit, o):
        return {
            "val": ctx.val,
            "type": "int"
        }

    def visitFloatLit(self, ctx, o):
        return {
            "val": ctx.val,
            "type": "float"
        }

    def visitBoolLit(self, ctx, o):
        return {
            "val": ctx.val,
            "type": "bool"
        }

    def visitId(self, ctx, o):
        return {
            "val": ctx.name,
            "type": None
        }

# class StaticCheck(Visitor):

#     def visitBinOp(self, ctx: BinOp, o):
#         o = []
#         left = self.visit(ctx.e1, o)
#         right = self.visit(ctx.e2, o)

#         while (type(left) is (BinOp or UnOp)):
#             left = self.visit(left)
#         while (type(right) is (BinOp or UnOp)):
#             right = self.visit(right)

#         if (ctx.op == "+" or ctx.op == "-" or ctx.op == "*"):
#             # Check input
#             if (not (type(left) is (int or float)) or not (type(right) is (int or float))):
#                 raise TypeMismatchInExpression(ctx)

#             # Check output
#             if (type(left) is float or type(right) is float):
#                 if (ctx.op == "+"):
#                     return float(left + right)
#                 if (ctx.op == "-"):
#                     return float(left - right)
#                 if (ctx.op == "*"):
#                     return float(left * right)
#             else:
#                 if (ctx.op == "+"):
#                     return int(left + right)
#                 if (ctx.op == "-"):
#                     return int(left - right)
#                 if (ctx.op == "*"):
#                     return int(left * right)
#         elif (ctx.op == "/"):
#             if (not (type(left) is (int or float)) or not (type(right) is (int or float))):
#                 raise TypeMismatchInExpression(ctx)
#             return float(left / right)
#         elif (ctx.op == "&&" or ctx.op == "||"):
#             if (not (type(left) is bool) or (not (type(right) is bool))):
#                 raise TypeMismatchInExpression(ctx)
#             if (ctx.op == "&&"):
#                 return bool(left and right)
#             if (ctx.op == "||"):
#                 return bool(left or right)
#         else:
#             # < > == or !=
#             if (not(type(left) is type(right))):
#                 raise TypeMismatchInExpression(ctx)
#             if (ctx.op == "<"):
#                 return left < right
#             if (ctx.op == ">"):
#                 return left > right
#             if (ctx.op == "=="):
#                 return left == right
#             if (ctx.op == "!="):
#                 return not (left == right)

#     def visitUnOp(self, ctx: UnOp, o):
#         o = []
#         val = self.visit(ctx.e, o)

#         while (type(val) is (BinOp or UnOp)):
#             val = self.visit(val)
#         if (ctx.op == "-"):
#             # + -  *
#             if (not (type(val) is (int or float))):
#                 raise TypeMismatchInExpression(ctx)
#             if (type(val) is float):
#                 if (ctx.op == "-"):
#                     return float(val)
#             else:
#                 if (ctx.op == "-"):
#                     return int(val)

#         if (ctx.op == "!"):
#             # + -  *
#             if (not (type(val) is bool)):
#                 raise TypeMismatchInExpression(ctx)

#             return bool(not val)

#     def visitIntLit(self, ctx: IntLit, o):
#         return ctx.val

#     def visitFloatLit(self, ctx, o):
#         return ctx.val

#     def visitBoolLit(self, ctx, o):
#         return ctx.val
