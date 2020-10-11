from random import randint

def rand5():
    return randint(1,5)

def rand7():
    rand = rand5()
    if randint(1, 6) == 1:
        rand = 6
    if randint(1, 7) == 1:
        rand = 7
    return rand

from collections import defaultdict
freq = defaultdict(int)
for _ in range(50):
    freq[rand7()] += 1
print(freq)

freq = defaultdict(int)
for _ in range(50):
    freq[randint(1, 7)] += 1
print(freq)