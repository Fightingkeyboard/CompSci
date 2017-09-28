def encode_letter(c,r):
    x = ord(c) + r % 26
    y = ord(c) + r % -26
    encoded = 0
    
    if c.islower():
        if r >= 0:
            if x > ord('z'):
                encoded += x - 26
            else:
                encoded = x
        else:
            if y < ord('a'):
                encoded += y + 26
            else:
                encoded = y
    elif c.isupper() and r>= 0:
        if r >= 0:
            if x > ord('Z'):
                encoded += x -26
            else:
                encoded = x
        else:
            if y < ord('A'):
                encoded += y + 26
            else:
                encoded = y
    return chr(encoded)

def encode_string(s,r):
    encoded=''
    for x in range(0,len(s)):
        if s[x].isalpha():
            encoded += encode_letter(s[x],r)
        else:
            encoded+=s[x]
    return encoded

def full_encode(s):
    encoded = ''
    for x in range(26):
        encoded += encode_string(s,x) + '\n'
    return encoded

print (encode_letter('h', -10) + '\n')
print (encode_string('Hello123', 16) + '\n')
print (full_encode('encoded123') + '\n')