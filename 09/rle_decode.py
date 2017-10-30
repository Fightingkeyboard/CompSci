def rle_decode(l):
    decoded = ''
    for i in range(len(l)):
        if str(l[i]).isalpha():
            if i == 0 or str(l[i-1]).isalpha():
                decoded += l[i]
            else:
                decoded += l[i-1]*l[i]
    return decoded
print (rle_decode([2,'a',3,'b','c',2,'d']))