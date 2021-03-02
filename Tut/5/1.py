def doubleA(lst):
    return [x*2 for x in lst]


def doubleB(lst):
    if len(lst) == 0:
        return lst
    else:
        return [lst[0]*2] + doubleB(lst[1:])


def doubleC(x):
    return list(map(lambda lst: lst * 2, x))
