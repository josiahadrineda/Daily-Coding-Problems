def valid_parentheses(parentheses):
    stack = ''
    for char in parentheses:
        stack += char
        while '()' in stack:
            stack = stack[:-2]
    return len(stack)

res = valid_parentheses('((()))')
assert res == 0, str(res) + ' is not equal to 0.'
res = valid_parentheses('()())()')
assert res == 1, str(res) + ' is not equal to 1.'
res = valid_parentheses(')(')
assert res == 2, str(res) + ' is not equal to 2.'