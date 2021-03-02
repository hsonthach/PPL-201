from functools import reduce


def support(a, b):
    print(a, b)
    if (len(a) == 0):
        return [b]
    return a + [a[-1]+b]


def combine(lst1, lst2):
    if (len(lst1) <= 1):
        return [(lst1[0], lst2[0])]

    return [(lst1[0], lst2[0])] + combine(lst1[1::], lst2[1::])


lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

#print(reduce(support, lst, []))
print(combine(lst1, lst2))
