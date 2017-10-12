def freq(n,l):
    x = 0
    for i in l:
        if n == i:
            x += 1
    return x

print (freq(3,[3,2,2,1,3,4,5,4,3,4,3]))

def min(l):
    x = l[0]
    for i in l:
        if i < x:
            x = i
    return x

print (min([9,60,10,4,5]))

def mode(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    y = []
    for i in x:
        y.append(freq(i,l))
    z = 0
    for i in y:
        if i > z:
            z = i
    return x[y.index(z)]

print (mode([1,1,1,4,4,9,20,20,20,20,20,2,2,3,3,9]))