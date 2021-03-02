class O:
    def __init__(self):
        self.__name = "Son"

    def printName(self):
        print(self.__name)


class A(O):
    def foo(self):
        print("a")


class B(O):

    pass


class C(O):
    def foo(self):
        print("c")
    pass


class D(A, B):
    def __init__(self):
        self.__name = "Test"

    def printName(self):
        print(self.__name)


class E(C, A):

    pass
# invalid
# class F(D,B,E):
#     pass
# valid


class F(D, E, B):
    pass


x = F()
x.printName()
print(type(x) is A)
print(isinstance(x, A))
