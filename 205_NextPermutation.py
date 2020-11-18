def next_permutation(num):
    """Given a positive integer NUM, computes the next permutation in
    absolute order. If NUM is the highest possible permutation, computes
    the lowest one (circular).

    >>> next_permutation(48975)
    49578
    >>> next_permutation(54321)
    12345
    """
    assert num > 0, 'NUM must be a positive integer.'

    if num < 10:
        return num

    num_list = decompose(num)
    
    i, j = len(num_list) - 1, len(num_list) - 1
    while i > 0 and num_list[i-1] >= num_list[i]:
        i -= 1
    if i == 0:
        return compose(num_list[::-1])

    k = i - 1
    while num_list[j] <= num_list[k]:
        j -= 1
    num_list[j], num_list[k] = num_list[k], num_list[j]

    num_list[k+1:] = num_list[k+1:][::-1]
    return compose(num_list)


def compose(num_list):
    num, mul = 0, 1
    for n in num_list[::-1]:
        num += n * mul
        mul *= 10
    return num

def decompose(num):
    num_list = []
    while num:
        last, num = num % 10, num // 10
        num_list.insert(0, last)
    return num_list