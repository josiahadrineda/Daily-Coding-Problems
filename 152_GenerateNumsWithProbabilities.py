from random import random
from bisect import bisect_left

def generate_w_probs(nums, probs):
    """Given a list of numbers NUMS and their corresponding probabilities
    PROBS, returns a number num from NUMS with PROBS[num] probability.

    >>> from collections import defaultdict
    >>> probs = defaultdict(int)
    >>> tests = 10000
    >>> for _ in range(tests):
    ...     num = generate_w_probs([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])
    ...     probs[num] += 1
    >>> round(probs[1] / tests, 1)
    0.1
    >>> round(probs[2] / tests, 1)
    0.5
    >>> round(probs[3] / tests, 1)
    0.2
    >>> round(probs[4] / tests, 1)
    0.2
    """
    assertions(nums, probs)

    cumulative_probs, tot = [], 0
    for prob in probs:
        tot += prob
        cumulative_probs.append(tot)

    rand = random()
    ind = bisect_left(cumulative_probs, rand)
    return nums[ind]
    

def assertions(nums, probs):
    assert nums, 'Cannot generate number from empty list.'
    for num in nums:
        assert isinstance(num, int), 'Number in NUMS must be an integer value.'
    for prob in probs:
        assert isinstance(prob, float), 'Probability must be a float value.'
        assert 0 <= prob <= 1, 'Probability must be between 0 and 1.'
    assert sum(probs) == 1.0, 'Sum of PROBS must be equal to 1.'
    assert len(nums) == len(probs), 'NUMS and PROBS must be of the same length.'