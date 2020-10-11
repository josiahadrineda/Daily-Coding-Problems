def perfect_number(n):
    a = n
    b = 10 - sum([int(c) for c in str(a)])
    try:
        return int(str(a) + str(b))
    except:
        return -1

for i in range(20):
    print(perfect_number(i))