def encode(s):
    encoded = []
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        if count == 0 and s[i] != s[i+1]:
            encoded.append(s[i])
        elif count != 0:
            if s[i] != s[i+1]:
                count += 1
                encoded.append(count)
                encoded.append(s[i])
                count = 0
        if i == len(s)-2 and s[i] == s[len(s)-1]:
            count += 1
            encoded.append(count)
            encoded.append(s[i+1])
        elif i == len(s)-2 and s[i] != s[len(s)-1]:
            encoded.append(s[i+1])
    return encoded
print (encode('abababa'))
print (encode('aaccaaabb'))
print (encode("aabcccdeeeeaaa"))
