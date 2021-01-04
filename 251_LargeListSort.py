# https://www.geeksforgeeks.org/timsort/

def sort(nums):
    """Given a list of a million integers between 0 and 10**9 NUMS,
    efficiently sorts NUMS.

    >>> from random import shuffle
    >>> nums = list(range(10**6))
    >>> shuffle(nums)
    >>> sort(nums)
    >>> nums == list(range(10**6))
    True
    """
    assert nums, 'NUMS cannot be an empty list.'

    def timsort(nums):
        MIN_MERGE = 32

        def calc_min_run(n):
            r = 0
            while n >= MIN_MERGE: 
                r |= n & 1
                n >>= 1
            return n + r

        def insertion_sort(nums, l, r):
            for i in range(l + 1, r + 1):
                j = i
                while j > l and nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                    j -= 1

        def merge_sort(nums, l, m, r):
            n1, n2 = m - l + 1, r - m
            l1, l2 = [], []
            for i in range(0, n1):
                l1.append(nums[l + i])
            for i in range(0, n2):
                l2.append(nums[m + 1 + i])

            i, j, k = 0, 0, l
            while i < n1 and j < n2:
                if l1[i] <= l2[j]:
                    nums[k] = l1[i]
                    i += 1
                else:
                    nums[k] = l2[j]
                    j += 1
                k += 1

            while i < n1:
                nums[k] = l1[i]
                i += 1
                k += 1

            while j < n2:
                nums[k] = l2[j]
                j += 1
                k += 1

        n = len(nums)
        min_run = calc_min_run(n)

        for s in range(0, n, min_run):
            e = min(s + min_run - 1, n - 1)
            insertion_sort(nums, s, e)

        size = min_run
        while size < n:
            for l in range(0, n, 2 * size):
                m = min(l + size - 1, n - 1)
                r = min(l + 2 * size - 1, n - 1)
                merge_sort(nums, l, m, r)
            size *= 2

    timsort(nums)