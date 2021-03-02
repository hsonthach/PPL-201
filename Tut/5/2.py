from functools import reduce
import itertools

lst = [[0, 1], [2, 3]]


def flattenA(lst):
    return list(itertools.chain.from_iterable(lst))
    

def flattenB(lst):
    if lst:
        return lst[0] + flattenB(lst[1:])
    else:
        return []

def func (x,y): 
    return x+y 

def flattenC(lst):
    return list(reduce(lambda x, y: x + y, lst,[]))


#[[1, 2, 3], [1.1, 2.1, 3.1]]
# [] + [1,2,3] = [1,2,3]
# [1,2,3] + [4,5,6] = [1->6]

print(flattenC([[1, 2, 3], [1.1, 2.1, 3.1]]))
