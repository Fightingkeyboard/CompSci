#Anthony % Anton Madlibs

story = 'The ADJ NOUN was VERB because the NOUN did not like the ADJ NOUN VERB at NOUN'
nouns = ['dude', 'man', 'kid']
verbs = ['fighting', 'racing', 'running']
adj = ['blue', 'happy', 'sad']

import random as rand
s = ['NOUN', 'VERB', 'ADJ']
l = [nouns, verbs, adj]
for x in range(len(s)):
    while story.find(s[x]) != -1:
        rand.shuffle(l[x])
        num = story.find(s[x])
        story = story[:num] + (l[x])[0] + story[num+len(s[x]):]

print (story)