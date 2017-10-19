import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input ().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

def fruit_on_house(fruit,times,tree_position):
    count = 0
    for i in range(times):
        if fruit[i] + tree_position >= s and fruit[i] + tree_position <= t:
            count += 1
    return count

print (fruit_on_house(apple,m,a))
print (fruit_on_house(orange,n,b))