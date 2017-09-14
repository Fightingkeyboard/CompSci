def string_times(str, n):
    return str*n

def front_times(str, n):
    result=''
    x=0
    front=(str[0:3])
    while (x<n):
        result+=front
        x+=1
    return result

def string_bits(str):
    return str[0::2]

def lone_sum(a, b, c):
    if (a==b):
        if (a==c):
            return 0
        return c
    if (a==c):
        return b
    if (b==c):
        return a
    return a+b+c

def string_splosion(str):
    if (len(str) == 1):
        return str
    
def string_splosion(str):
    if (len(str) == 1):
        return str
    if (len(str) == 2):
        return str[0]*2+str[1]
    if (len(str) == 3):
        return str[0]*2+str[1]+str
    if (len(str) == 4):
        return str[0]*2+str[1]+str[0:3]+str
    if (len(str) == 5):
        return str[0]*2+str[1]+str[0:3]+str[0:4]+str
    if (len(str) == 6):
        return str[0]*2+str[1]+str[0:3]+str[0:4]+str[0:5]+str
    return "don't care situation"

def cigar_party(cigars, is_weekend):
    if is_weekend:
        if (cigars < 40):
            return False
        return True
    if (cigars < 40):
        return False
    if (cigars > 60):
        return False
    return True

def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed < 66:
            return 0
        if speed > 85:
            return 2
        return 1
    if speed < 61:
        return 0
    if speed > 80:
        return 2
    return 1

print(string_times('hi', 2))
print(front_times('chocolate', 2))
print(string_bits('hello'))
print(lone_sum(1,2,2))
print(string_splosion('code'))
print(cigar_party(61, False))
print(caught_speeding(85, True))