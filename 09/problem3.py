def score(w):
    w = w.upper()
    total = 0
    scoremaster = {'AEIOULNRST': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10}
    for i in w:
        for v in scoremaster.keys():
            if i in v:
                total += scoremaster[v]
    return total
        
print(score('AEI'))
print(score('hello'))
print(score('HELLO'))
print(score('AEIOU'))
print(score('aEIoZ'))
print(score(''))