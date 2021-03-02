from functools import reduce


def lessThan(n, lst):
    return [ele for ele in lst if ele < n]


def lessThan(n, lst):
    if lst:
        return lessThan_b(n, lst[1:]) if lst[0] >= n \
            else [lst[0]] + lessThan_b(n, lst[1:])
    else:
        return []


def lessThan(n, lst):
    return list(filter(lambda ele: ele < n, lst))
