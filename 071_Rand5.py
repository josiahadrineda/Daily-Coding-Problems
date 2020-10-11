from random import randint
from collections import defaultdict

def rand7():
    return randint(1,7)

def rand5():
    rand = rand7()
    while rand == 6 or rand == 7:
        rand = rand7()
    return rand

ones = 0
tot = 0
for _ in range(1000000):
    if rand5() == 1:
        ones += 1
    tot += 1

print(ones / tot)