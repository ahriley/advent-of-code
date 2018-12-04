import numpy as np
from collections import Counter

with open('data/day2.txt') as f:
    lines = f.readlines()

# part 1
phrases = [line.strip('\n') for line in lines]
counters = [dict(Counter(phrase)) for phrase in phrases]
results = [[c[key] for key in c.keys()] for c in counters]
twos = np.array([2 in result for result in results])
threes = np.array([3 in result for result in results])
print(np.sum(twos)*np.sum(threes))

# part 2
assert (np.array([len(phrase) for phrase in phrases]) == len(phrases[0])).all()
charlist = np.array([list(phrase) for phrase in phrases])

for i in range(len(charlist)):
    for j in range(i+1,len(charlist)):
        if np.sum(charlist[i] == charlist[j]) == len(charlist[i]) - 1:
            word1 = charlist[i]
            word2 = charlist[j]

answer = word1[word1 == word2]
print(''.join(answer))
