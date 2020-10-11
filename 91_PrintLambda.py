functions = []
for i in range(10):
    functions.append(lambda : i)

"""
functions.append(
    def lambda():
        return i
)
"""

for f in functions:
    print(f())

"""
Assumption: By the end of for loop 1, i will be set to 10. Therefore the second for loop will print 10 ten times.
Correction: i actually becomes 9, not 10. Apparently Python for loops work by checking if the increment/decrement expression w/ the var meets the condition before binding it.
"""

better_functions = []
for i in range(10):
    better_functions.append(lambda i: i)

for i in range(10):
    print(better_functions[i](i))

"""
better_functions2 = []
for i in range(10):
    better_functions2.append(lambda : i)

i = 0
for f in better_functions2:
    print(f())
    i += 1
"""