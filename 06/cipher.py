import math

real_freq = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

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

def derotate(s):
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
print (derotate(test))