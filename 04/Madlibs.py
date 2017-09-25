#Anthony % Anton Madlibs

story = 'NAME was VERB because NAME did not like the NAME VERB at NOUN. So NAME went to NOUN, but NOUN was not a place for VERB. The end.'
names = ['dude', 'man', 'kid']
verbs = ['fighting', 'racing', 'running']
nouns = ['Hardware Store', 'School', 'Heliport']

import random as rand
s = ['NOUN', 'VERB', 'NAME']
l = [nouns, verbs, names]
for x in range(len(s)):
    while story.find(s[x]) != -1:
        rand.shuffle(l[x])
        num = story.find(s[x])
        story = story[:num] + (l[x])[0] + story[num+len(s[x]):]

print (story)