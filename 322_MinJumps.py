# https://leetcode.com/problems/reach-a-number/discuss/112968/Short-JAVA-Solution-with-Explanation

def min_jumps(n):
    """Starting from 0 on a number line, you would like to make a series of jumps that
    lead to the integer N. On the ith jump, you may move exactly i places to the left
    or right. Returns the minimum number of jumps required to reach N.

    >>> for x in range(1, 11):
    ...     print(min_jumps(x)) 
    1
    3
    2
    3
    5
    3
    5
    4
    5
    4
    """
    
    n = abs(n)

    step, tot = 0, 0
    while tot < n:
        step += 1
        tot += step
    while (tot - n) % 2 == 1:
        step += 1
        tot += step
    return step