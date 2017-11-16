import random

def buildwordlist(text):
    l = []
    for w in text.split():
        w = w.lower()
        word = ''
        for x in w:
            if x.isalpha():
                word += x
        if word != '':
            l.append(word)
    return l

def buildwordphrasedictionary(text,length):
    text = open(text).read()
    pd = {}
    l = buildwordlist(text)
    for i in range(len(l)-length):
        key = (" ".join(l[i:i+length]))
        value = l[i+length]
        pd.setdefault(key,[])
        pd[key].append(value)
    return pd

def bwpdhuman(text,length):
    d = buildwordphrasedictionary(text,length)
    k = list(d.keys())
    v = list(d.values())
    for i in range(len(k)):
        r = print(k[i], ':', v[i])
    return r

def generate_text(d,start_word,length=50):
    wordlist = []
    next = start_word
    for i in range(length):
        if next not in d:
            break
        wordlist.append(next)
        next = random.choice(d[next])
    return " ".join(wordlist)

bwpdhuman('hamlet.txt',2)
bwpdhuman('hamlet.txt',3)
bwpdhuman('sonnets.txt',2)
bwpdhuman('sonnets.txt',3)
bwpdhuman('psalms.txt',2)
bwpdhuman('psalms.txt',3)