from functools import reduce


def test(a, b):
    print(a)
    print(b)
    return a + b


lst = [1, 2, 3, 4, 5]

reduce(test, lst, 0)
