def PigLatin(str):
    vowels = 'aeiou'
    if str[0] not in vowels:
        str = str[1:] + str[0] + 'ay'
        return (str)
    else:
        return str + 'ay'