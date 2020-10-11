import random

def approximate(N):
    tot = 0

    for i in range(N):
        x,y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            tot += 1
    
    #Multiply by 4 because r = 0.5 (square is 1x1). Area of the circle is PI / 4
    #PI / 4 == tot / N, therefore PI == 4 * (tot/N)
    return round(4 * (tot/N), 3)

print(approximate(10000000))