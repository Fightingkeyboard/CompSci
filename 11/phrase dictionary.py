def buildwordlist(text):
    l = []
    d = {}
    for w in text.split():
        w = w.lower()
        word = ''
        for x in w:
            if x.isalpha():
                word += x
        if word != '':
            l.append(word)
    return l

def buildwordphrasedictionary(text):
    text = open(text).read()
    pd = {}
    l = buildwordlist(text)
    for i in range(len(l)-1):
        pd.setdefault(l[i],list())
        pd[l[i]].append(l[i+1])
    return pd