from functools import reduce

# def double(list):
#     return [el*2 for el in list]
# def double(list):
#     result = []
#     if (len(list) == 0):
#         return []
#     return [list[0]*2] + double(list[1:])
# def double(lst):
#     return list(map(lambda el: el*2, lst))


# def flatten(lst):
#     return list(reduce(lambda a, b: a + b, lst, []))

# def lessThan(n, lst):
#     return [el for el in lst if (el < n)]

# def lessThan(n, lst):
#     if (len(lst) == 0):
#         return []
#     if (lst[0] < n):
#         return[lst[0]] + lessThan(n, lst[1:])
#     return lessThan(n, lst[1:])


# def lessThan(n, lst):
#     def lessThanHelper(a, b):
#         print(a, b)
#         if (b < n):
#             return a + [b]
#         return a + []

#     return reduce(lambda a, b: a + [b] if (b < n) else a + [], lst, [])


def square(num):
    return num * num


def increase(num):
    return num + 1


def double(num):
    return num * 2


def compose(*args):
    def h(x):
        def helper(a, b):
            return b(a)
        return reduce(helper, reversed(args), x)
    return h
    # return reduce(lessThanHelper, lst, [])

# def flatten(lst):
#     if (len(lst) == 0):
#         return []
#     return lst[0] + flatten(lst[1:])

# def flatten(lst):
#     # [1,2,3]
#     result = []
#     [result.append(child) for el in lst for (child) in el]
#    return result


#result = double([5, 7, 12, -4])
#result = flatten([[1, 2, 3], ['a', 'b', 'c'], [1.1, 2.1, 3.1]])

#result = lessThan(50, [1, 55, 6, 2])
result = compose(square, increase, double)(2)

print(result)
