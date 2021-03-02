from functools import reduce


def square(num):
    return num * num


def increase(num):
    return num + 1


def double(num):
    return num * 2


def composeA(*args):
    cps = composeA(*args[:-1]) if len(args) > 2 else args[-2]
    return lambda num: cps(args[-1](num))


def composeB(*args):
    def h(arg):
        return reduce(lambda x, y: y(x), reversed(args), arg)
    return h


print(composeA(square, increase, double)(2))
print(composeB(square, increase, double)(2))
