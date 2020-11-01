def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()

"""
1. make_functions func is defined and bound to make_functions
2. make_functions is called
    A. flist is instantiated as an empty list
    B. i is iterated upon with 1, 2, then 3
        a. print_i func is defined and bound to print_i
        b. print_i function itself is appended to flist
    C. flist is returned
3. The resulting flist is bound to functions
4. f is iterated upon with each function (print_i) in functions

Expected Output:
3
3
3

Reasoning:
Each print_i does not save the current state of i. Instead, they only have a reference to i
once i has finished iterating - that is, when i is bound to the last element of the list, 3.
We want to figure out a way to save the current state of i to print 1, 2, then 3.
"""

# What we want to have happen

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i_maker(i):
            def print_i():
                print(i)
            return print_i
        flist.append(print_i_maker(i))

    return flist

functions = make_functions()
for f in functions:
    f()

"""
The difference between this rendition and the last one is the use of another layer of HOF - the
first layer instantiating the creation of functions, the second layer saving the current state of i,
and the last layer finally doing the printing.
"""