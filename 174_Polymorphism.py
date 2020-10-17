# https://en.wikipedia.org/wiki/Polymorphism_(computer_science)

"""
Primary Types of Polymorphism:

Ad-Hoc - Non-fundamental feature of the type system in that multiple functions
can be used to implement the same behavior over different types

ex. In a non-dynamically typed language: add(int, int) and add(str, str) may
reference different functions

Parametric - Allows a function or object to account for muliple types (generic)

ex. The list data structure [3, 'foo', lambda : bar()]

Subtype - Provides functionality for subtypes of a certain object as well as the
object itself

ex. Class inheritance (aka whatever attributes/methods aren't found within a
particular subclass can be traced back to its superclass(es))
"""