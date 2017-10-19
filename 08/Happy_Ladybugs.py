'''
b = board = str
n = length of b
b[i] = board[i]
if b[i] = _ = empty
if b[i] = alpha.upper = board[i] has ladybug of color b[i]
ladybug is happy when b[i]+-1 has a ladybug of the same color
ladybug can move to and empty cell in 1 move
g = games
Can you make all ladybugs happy?
'''

import sys

def has_space(s):
    space = False
    if '_' in s:
        space = True
    return space

def correct_color(s):
    l1 = []
    multiple = True
    for i in s:
        l1.append(i)
    l1[:] = (value for value in l1 if value != '_')
    s1 = set(l1)
    for i in s1:
        if l1.count(i) < 2:
            multiple = False
    if has_space(s) and multiple:
        return 'YES'
    elif has_space(s) == False and multiple:
        for i in range(len(s)):
            if i == 0 and i != s[i+1]:
                return 'NO'
            elif s[i] != s[i-1] or s[i+1]:
                return 'NO'
            else:
                return 'YES'
    else:
        return 'NO'
            
g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    b = input().strip()
    print (correct_color(b))


