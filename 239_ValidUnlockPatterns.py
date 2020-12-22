COMBOS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

def valid_unlock_patterns():
    """Returns the total number of possible valid unlock patterns
    for a smartphone (keypad labeled 1-9, example below).

    1 2 3
    4 5 6
    7 8 9

    >>> valid_unlock_patterns()
    389112
    """

    def is_valid(nums, curr, num_to_add):
        for c in COMBOS:
            f, v, t = c
            if v in nums:
                if f == num_to_add and t in curr[-1:]:
                    return False
                if t == num_to_add and f in curr[-1:]:
                    return False
        return True

    def valid_unlock_patterns_recur(nums, curr):
        if len(curr) >= 4:
            patterns.add(tuple(curr))
        for i, num in enumerate(list(nums)):
            if is_valid(nums, curr, num):
                nums.remove(num)
                valid_unlock_patterns_recur(nums, curr + [num])
                nums.insert(i, num)

    patterns = set()
    valid_unlock_patterns_recur([1, 2, 3, 4, 5, 6, 7, 8, 9], [])
    return len(patterns)