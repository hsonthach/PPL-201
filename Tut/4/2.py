from abc import ABC


class Expr(ABC):
    pass


class Var(Expr):
    def __init__(self, name="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name


class BinExp(Expr):
    def __init__(self, left, operator, right, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = operator
        self.left = left.eval()
        self.right = right.eval()

    def eval(self):

        while (isinstance(self.left, Expr)):
            self.left = self.left.eval()
        while (isinstance(self.right, Expr)):
            self.right = self.right.eval()

        if self.operator == "+":
            return IntLit(self.left + self.right).eval()
        elif self.operator == "-":
            return IntLit(self.left - self.right).eval()
        elif self.operator == "*":
            return IntLit(self.left * self.right).eval()
        elif self.operator == "/":
            return IntLit(self.left / self.right).eval()


class UnExp(Expr):
    def __init__(self, operator,  num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = operator
        self.num = num.eval()

    def eval(self):
        if (isinstance(self.num, Expr)):
            self.num = self.num.eval()

        if self.operator == "+":
            return IntLit(+self.num).eval()
        elif self.operator == "-":
            return IntLit(-self.num).eval()


class IntLit(Expr):
    def __init__(self, num):
        self.num = num

    def print(self):
        print(self.num)  # print number attribute

    def eval(self):
        return self.num


class FloatLit(Expr):
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num
