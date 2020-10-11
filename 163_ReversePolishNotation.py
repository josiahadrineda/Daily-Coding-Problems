from operator import add, sub, mul, truediv

def evaluate(exp):
    """Given an arithmetic expression in Reverse Polish Notation EXP,
    evaluates said expression.

    >>> evaluate([5, 3, '+'])
    8
    >>> evaluate([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'])
    5
    """
    for val in exp:
        assert isinstance(val, int) or val in '+-*/', 'Invalid operator/operand in EXP.'

    i = 2
    while len(exp) > 1:
        if isinstance(exp[i], str) and exp[i] in '+-*/':
            operand1, operand2 = exp.pop(i-2), exp.pop(i-2)
            operator = exp.pop(i-2)
            calc = perform_arithmetic(operator, operand1, operand2)

            i -= 1
            exp.insert(i-1, calc)
        else:
            i += 1

    return int(exp[0]) if int(exp[0]) == exp[0] else exp[0]

def perform_arithmetic(operator, operand1, operand2):
    """Performs an arithmetic computation based on one set
    of Reverse-Polish-Notated values (1 operator, 2 operands).
    """

    operators = {'+': add, '-': sub, '*': mul, '/': truediv}
    return operators[operator](operand1, operand2)