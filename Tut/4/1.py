from abc import ABC

prefixEx = []


class Expr(ABC):
    # def __init__(self, prefixEx="", *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     prefixEx = prefixEx

    def appendIntoPrefixEx(self, item):
        prefixEx.append(str(item))

    def printPrefix(self):
        
        self.traverse()
        print(' '.join(prefixEx) + ' ')
        return ' '.join(prefixEx) + ' '


class BinExp(Expr):
    def __init__(self, left, operator, right, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = operator
        self.left = left
        self.right = right

    def traverse(self):
        self.appendIntoPrefixEx(self.operator)
        if (not isinstance(self.left, Expr)):
            self.appendIntoPrefixEx(self.left.eval())
        else:
            self.left.traverse()
        if (not isinstance(self.right, Expr)):
            self.appendIntoPrefixEx(self.right.eval())
        else:
            self.right.traverse()

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
        self.num = num

    def eval(self):
        if (isinstance(self.num, Expr)):
            self.num = self.num.eval()

        if self.operator == "+":
            return IntLit(+self.num).eval()
        elif self.operator == "-":
            return IntLit(-self.num).eval()

    def traverse(self):
        self.appendIntoPrefixEx(self.operator + '.')
        if (not isinstance(self.num, Expr)):
            self.appendIntoPrefixEx(self.num.eval())
        else:
            self.num.traverse()


class IntLit():
    def __init__(self, num):
        self.num = num

    def printPrefix(self):
        return str(self.num) + ' '

    def eval(self):
        return self.num


class FloatLit():
    def __init__(self, num):
        self.num = num

    def printPrefix(self):
        return str(self.num) + ' '

    def eval(self):
        return self.num


x1 = UnExp('-', IntLit(4))
x2 = BinExp(IntLit(3), '*', IntLit(2))
x3 = BinExp(x1, '+', x2)

x3.printPrefix()
# print(str('-'))
