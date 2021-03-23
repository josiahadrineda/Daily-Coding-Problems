"""
Comments:
- Apparently this was the first problem to be classified as NP-complete
    - That's why my 2^k approach is a valid one
- This could definitely be improved by transforming FORMULA into a graph and running some sort of
  traversal on it (I'm pretty sure there is an algorithm called Kosaraju's that deals with this)
"""

def is_valid_2CNF(formula):
    """A Boolean formula is said to be satisfiable if there is a way to assign truth values to each
    variable such that the entire formula evaluates to True. A 2-CNF formula is a type of formula
    created by chaining (_ OR _) tuples with ANDs [for example (a or not b) and (b or not c) AND
    ...].
    
    Given a string representing a 2-CNF formula FORMULA, finds a way to assign truth values to
    satify it, or returns False if impossible.

    >>> is_valid_2CNF('(not c or b) and (b or c) and (not b or c) and (not c or not a)')
    [('a', False), ('b', True), ('c', True)]
    >>> is_valid_2CNF('(not a or b) and (a or not b) and (not a or not b)')
    [('a', False), ('b', False)]
    >>> is_valid_2CNF('(a or b) and (not a or b) and (a or not b) and (not a or not b)')
    False
    """
    assert formula, 'FORMULA cannot be an empty string.'

    vars = list(set(list(formula.replace('(', '').replace(')', '').replace('not', '').replace('or', '').replace('and', ''))))
    vars.remove(' ')
    vars.sort()

    n = len(vars)
    for i in range(2**n):
        temp_formula, cand = formula, []

        b_str = bin(i)[2:]
        b_str = '0' * (n - len(b_str)) + b_str
        for v,b in zip(vars, b_str):
            temp_formula = temp_formula.replace(' ' + v + ' ', ' ' + b + ' ').replace('(' + v, '(' + b).replace(v + ')', b + ')')
            cand.append((v, True if b == '1' else False))
        if eval(temp_formula):
            return cand
    return False