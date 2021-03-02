from abc import ABC, abstractmethod


class Expr(ABC):
    @abstractmethod
    def eval(self):
        """
        This abstract method should return a value
        :rtype: number (int, float, ...)
        """
        pass

    @abstractmethod
    def accept(self, visitor):
        pass


class Visitor(ABC):
    @abstractmethod
    def visit_BinExp(self, expr):
        pass

    @abstractmethod
    def visit_UnExp(self, expr):
        pass

    @abstractmethod
    def visit_IntLit(self, expr):
        pass

    @abstractmethod
    def visit_FloatLit(self, expr):
        pass


class BinExp(Expr):
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right
        pass

    def eval(self):
        if self.operator == "+":
            return self.left.eval() + self.right.eval()
        elif self.operator == "-":
            return self.left.eval() - self.right.eval()
        elif self.operator == "*":
            return self.left.eval() * self.right.eval()
        elif self.operator == "/":
            return self.left.eval() / self.right.eval()
        else:
            pass

    def accept(self, visitor: Visitor):
        return visitor.visit_BinExp(self)


class UnExp(Expr):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
        pass

    def eval(self):
        if self.operator == "+":
            return self.operand.eval()
        elif self.operator == "-":
            return -1 * self.operand.eval()

    def accept(self, visitor: Visitor):
        return visitor.visit_UnExp(self)


class IntLit(Expr):
    def __init__(self, Val):
        self.Val = int(Val)
        pass

    def eval(self):
        return self.Val

    def accept(self, visitor: Visitor):
        return visitor.visit_IntLit(self)


class FloatLit(Expr):
    def __init__(self, Val):
        self.Val = float(Val)
        pass

    def eval(self):
        return self.Val

    def accept(self, visitor: Visitor):
        return visitor.visit_FloatLit(self)


"""
        This function need to know what class caller is,
        to return the correct type of visitor to work!

        How could no information retained and still can call:

        x.accept(Eval()) ??

        _____________________
        WELL as it turned out, Eval() was an un-explicit object creation
        Fork that, 
"""


class Eval(Visitor):
    def visit_BinExp(self, expr):
        if expr.operator == "+":
            return expr.left.accept(self) + expr.right.accept(self)
        elif expr.operator == "-":
            return expr.left.accept(self) - expr.right.accept(self)
        elif expr.operator == "*":
            return expr.left.accept(self) * expr.right.accept(self)
        elif expr.operator == "/":
            return expr.left.accept(self) / expr.right.accept(self)
        else:
            pass
        pass

    def visit_UnExp(self, expr):
        if expr.operator == "+":
            return expr.operand.accept(self)
        elif expr.operator == "-":
            return -1 * expr.operand.accept(self)
        pass

    def visit_IntLit(self, expr):
        return expr.Val

    def visit_FloatLit(self, expr):
        return expr.Val

    pass


class printPrefix(Visitor):
    def visit_BinExp(self, expr):
        s = expr.operator + ' '
        s += expr.left.accept(self)
        s += expr.right.accept(self)
        return s

    def visit_UnExp(self, expr):
        s = expr.operator + ". "
        s += expr.operand.accept(self)
        return s

    def visit_IntLit(self, expr):
        return str(expr.Val) + ' '

    def visit_FloatLit(self, expr):
        return str(expr.Val) + ' '

    pass


class printPostfix(Visitor):
    def visit_BinExp(self, expr):
        s = expr.left.accept(printPrefix())
        s += expr.right.accept(printPrefix())
        s += expr.operator + ' '
        return s

    def visit_UnExp(self, expr):
        s = expr.operand.accept(printPrefix())
        s += expr.operator + ". "
        return s

    def visit_IntLit(self, expr):
        return str(expr.Val) + ' '

    def visit_FloatLit(self, expr):
        return str(expr.Val) + ' '

    pass


def testcase_1():
    A = IntLit(1)
    B = IntLit(2)
    C = IntLit(3)
    D = IntLit(4)
    F = FloatLit(2.0)
    expr0 = BinExp(C, '-', D)
    expr1 = BinExp(B, '*', expr0)
    expr2 = BinExp(A, '+', expr1)
    expr3 = BinExp(F, '*', expr2)
    expr4 = UnExp('-', expr3)

    evaluate = Eval()
    prefix = printPrefix()
    postfix = printPostfix()
    print("_________________")
    print(A.accept(evaluate))
    print(A.accept(prefix))
    print(A.accept(postfix))
    print("_________________")
    print(F.accept(evaluate))
    print(F.accept(prefix))
    print(F.accept(postfix))
    print("_________________")
    print(expr3.accept(evaluate))
    print(expr3.accept(prefix))
    print(expr3.accept(postfix))
    print("_________________")
    print(expr4.accept(evaluate))
    print(expr4.accept(prefix))
    print(expr4.accept(postfix))
    print("_________________")
    pass


if __name__ == "__main__":
    testcase_1()

    pass
testcase_1()
