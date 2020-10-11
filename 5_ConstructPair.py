def cons(a, b):
    def pair(f):
        return f(a, b) #Calls f, passing in a and b
    return pair #Returns f(a, b)

#We need some function to pass to f to extract either a or b
def car(f):
    def left(a, b):
        return a
    return f(left)

def cdr(f):
    def right(a, b):
        return b
    return f(right)

#Quicker implementation
def car(f):
    return f(lambda a, b: a)

def cdr(f):
    return f(lambda a, b: b)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))