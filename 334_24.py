"""
Comments:
 - This code is scalable, but since it is essentially a brute-force alg it doesn't scale very well
"""

def twenty_four(nums):
    """Given a list of four integers NUMS, where each integer in NUMS is between 1 and 9,
    determines whether or not operators (+, -, *, /) can be placed between the integers
    and grouped with parentheses such that the value 24 is reached.

    >>> twenty_four([5, 2, 7, 8])   # (5 * 2 - 7) * 8
    True
    >>> twenty_four([1, 1, 1, 1])
    False
    """
    assert nums, 'NUMS cannot be an empty list.'

    def backtrack(ops):
        if len(ops) == (n - 1):
            for i, op in enumerate(ops):
                expr[(i + 1) * 3] = op
            for i in range(n - 1):
                for j in range(i + 1, n):
                    expr[i * 3 - 1] = expr[i * 3]
                    expr[i * 3] = '('
                    expr[j * 3 + 2] = ')'
                    try:
                        if eval(''.join(expr)) == 24:
                            return True
                    except ZeroDivisionError as e:
                        pass
                    expr[i * 3] = expr[i * 3 - 1] if i * 3 - 1 >= 0 else ''
                    expr[i * 3 - 1] = ''
                    expr[j * 3 + 2] = ''
            return False
        else:
            for op in OPS:
                if backtrack(ops + [op]):
                    return True
            return False

    n = len(nums)
    expr = [''] * (n * 3)
    for i in range(n):
        expr[i * 3 + 1] = str(nums[i])
    
    OPS = '+-*/'
    return backtrack([])