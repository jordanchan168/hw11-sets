'''
Jordan Chan
SoftDev2 pd 8
HW#11 -- Ready, Set, Math!
2017-04-24
'''

a = [1,2,3]
b = [2,3,4]

def union(a,b):
    return [x for x in a]+[y for y in b if y not in a]

print union(a,b)


def intersection(a,b):
    return [x for x in a if x in b]

print intersection(a,b)


def setDiff(a,b):
    return [x for x in a if x not in b]

print setDiff(a,b)
print setDiff(b,a)


def symDiff(a,b):
    return setDiff(a,b)+setDiff(b,a)

print symDiff(a,b)


c = [1,2]
d = ['red', 'white']

def cartProd(a,b):
    return [(x,y) for x in a for y in b]

print cartProd(c,d)
