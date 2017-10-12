import math


def rotate_char(c,r):
    if c.isalpha():
        v = ord(c)
        if v > 96:
            v = (v - 97 + r) % 26
            v += 97
        else:
            v = (v - 65 + r) % 26
            v += 65
        return chr(v)
    else:
        return c

def rotate_string(s,r):
    rotated = ''
    for x in range(len(s)):
        if s[x].isalpha():
            rotated += rotate_char(s[x],r)
        else:
            rotated += s[x]
    return rotated

def distance(l1,l2):
    length = len(l1)
    if length > len(l2):
        length = len(l2)
    sum = 0
    for i in range(length):
        sum += (l1[i]-l2[i])**2
    return math.sqrt(sum)

def build_frequency_vector(s):
    num_letters = 0
    for i in range(len(s)):
        if s[i].isalpha():
            num_letters += 1
    v=[]
    for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        v.append(s.count(i) / num_letters)
    return v

f = open('text.txt')
s = f.read()
f.close()
real_freq = build_frequency_vector(s)

def decode(s):
    smallest_distance = distance(build_frequency_vector(rotate_string(s,25)), real_freq)
    smallest_distance_rotations = 25
    for x in range(26):
        shifted_str = rotate_string(s,x)
        letter_freq = build_frequency_vector(shifted_str)
        dist = distance(letter_freq, real_freq)
        if dist < smallest_distance:
            smallest_distance = dist
            smallest_distance_rotations = x
    return rotate_string(s, smallest_distance_rotations)

test_string = 'This is a test, I will rotate the test string 20 steps and attempt to decode it with my program. Punctuation also seems functional!'
test = rotate_string(test_string, 20)
print (decode(test))