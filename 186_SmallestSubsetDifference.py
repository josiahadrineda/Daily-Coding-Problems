def smallest_subset_difference(nums):
    """Given an array of positive integers NUMS, divides NUMS into two
    subsets such that the difference between the sum of the subsets
    is as small as possible.

    >>> a, b = smallest_subset_difference([5, 10, 15, 20, 25])
    >>> assert sum(a) == 35 or sum(a) == 40
    >>> assert sum(b) == 35 or sum(b) == 40
    >>> c, d = smallest_subset_difference([1, 1, 1, 1, 1, 5])
    >>> assert sum(c) == 5 and sum(d) == 5
    """
    assert nums, 'NUMS cannot be an empty list.'

    a, b, min = [], [], sum(nums)
    def subset_diff_recur(nums, curr, ind):
        nonlocal a, b, min

        diff = abs(sum(curr) - sum(nums))
        if diff < min:
            a, b, min = curr.copy(), nums.copy(), diff
        elif not nums or ind == len(nums):
            pass
        else:
            while ind < len(nums):
                curr.append(nums[ind])
                subset_diff_recur(nums[:ind] + nums[ind+1:], curr, ind)

                curr.pop()
                subset_diff_recur(nums, curr, ind + 1)
                
                ind += 1

    subset_diff_recur(nums, [], 0)
    return a, b