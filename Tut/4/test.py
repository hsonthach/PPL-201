from functools import reduce
from abc import ABC, abstractmethod
# def compose(f, g):
#     def func(x):
#         return f(g(x))
#     return func


# def inc(x):
#     return x+1


# def square(x):
#     return x*x


# t = compose(inc, square)

# print(t(3))
# def foo(x: Int, y: Int) = x * y


args = [3, 4, 5]

print(reduce(lambda x, y: x+y, args))
