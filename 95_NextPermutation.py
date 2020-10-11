from itertools import permutations

def next_permutation(digits):
    all_perms = sorted([list(perm) for perm in permutations(digits)], reverse=True)
    return all_perms[all_perms.index(digits)-1]

assert next_permutation([2,1,3]) == [2,3,1]
assert next_permutation([2,2,3]) == [2,3,2]
assert next_permutation([3,2,1]) == [1,2,3]

def next_permutation_backtrack(digits):
    if is_highest(digits):
        return digits[::-1]
    
    all_perms = backtrack_helper(sorted(digits), [], set())
    all_perms = sorted(list(all_perms), reverse=True)
    all_perms = [list(perm) for perm in all_perms]
    
    return all_perms[all_perms.index(digits)-1]

def is_highest(digits):
    for i in range(len(digits)-1):
        if digits[i+1] > digits[i]:
            return False
    return True or digits.count(digits[0]) == len(digits)

def backtrack_helper(digits, curr_digits, all_perms):
    if not digits:
        all_perms.add(tuple(curr_digits.copy()))
    else:
        i = 0
        while i < len(digits):
            curr_digit = digits.pop(i)
            curr_digits.append(curr_digit)

            all_perms = backtrack_helper(digits, curr_digits, all_perms)

            curr_digits.pop()
            digits.insert(i, curr_digit)
            i += 1
    return all_perms

assert next_permutation_backtrack([2,1,3]) == [2,3,1]
assert next_permutation_backtrack([2,2,3]) == [2,3,2]
assert next_permutation_backtrack([3,2,1]) == [1,2,3]

def next_permutation_quicker(digits):
    # Taken from previous backtracking solution
    if is_highest(digits):
        return digits[::-1]

    # Taken from my LeetCode
    def leetcode_next_perm(digits):
        i = len(digits)-1
        while digits[i] <= digits[i-1]:
            i -= 1
            
        potential_swap_digits = [digits[j] for j in range(i, len(digits)) if digits[j] > digits[i-1]]
        next_digit = min(potential_swap_digits)
        swap_ind = len(digits) - digits[::-1].index(next_digit) - 1
        digits[i-1], digits[swap_ind] = digits[swap_ind], digits[i-1]
        digits[i:] = sorted(digits[i:])

        return digits
    
    return leetcode_next_perm(digits)

assert next_permutation_quicker([2,1,3]) == [2,3,1]
assert next_permutation_quicker([2,2,3]) == [2,3,2]
assert next_permutation_quicker([3,2,1]) == [1,2,3]