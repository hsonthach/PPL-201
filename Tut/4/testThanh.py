from abc import ABC, abstractmethod


class Expr(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def eval(self):
        """
        This abstract method should return a value
        :rtype: number (int, float, ...)
        """
        pass

    @abstractmethod
    def printPrefix(self):
        """
        This abstract method should return a string
        :rtype: str
        """
        pass


class BinExp(Expr):
    def __init__(self, left, operator, right):
        super().__init__()
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
        pass

    def printPrefix(self):
        s = self.operator + ' '
        s += self.left.printPrefix()
        s += self.right.printPrefix()
        return s


class UnExp(Expr):
    def __init__(self, operator, operand):
        super().__init__()
        self.operator = operator
        self.operand = operand

    def eval(self):
        if self.operator == "+":
            return self.operand.eval()
        elif self.operator == "-":
            return -1 * self.operand.eval()

    def printPrefix(self):
        s = self.operator + ". "
        s += self.operand.printPrefix()
        return s


class IntLit(Expr):
    def __init__(self, Val):
        super().__init__()
        self.Val = int(Val)
        pass

    def eval(self):
        return self.Val
        pass

    def printPrefix(self):
        return str(self.Val) + ' '


class FloatLit(Expr):
    def __init__(self, Val):
        super().__init__()
        self.Val = float(Val)
        pass

    def eval(self):
        return self.Val

    pass

    def printPrefix(self):
        return str(self.Val) + ' '


if __name__ == "__main__":
    i4 = IntLit(4)
    i3 = IntLit(3)
    i2 = IntLit(2)

    expr1 = UnExp('-', i4)
    expr2 = BinExp(i3, '*', i2)
    expr3 = BinExp(expr1, '+', expr2)

    print(expr3.printPrefix())

    pass
