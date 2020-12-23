def minimum_swaps(people):
    """There are N couples sitting in a row of length 2N. They are currently
    ordered randomly, but would like to rearrange themselves so that each
    couple's partners can sit side by side. Computes the minimum number of
    swaps so as to accomplish this task.

    >>> people = [1, 3, 2, 3, 1, 2]
    >>> minimum_swaps(people)
    2
    """

    if not people:
        return 0
    elif people[0] == people[1]:
        return minimum_swaps(people[2:])
    else:
        num_a, num_b = people[0], people[1]
        people[0] = '#'
        ind_a = people.index(num_a)
        people[0] = num_a
        people[1] = '#'
        ind_b = people.index(num_b)
        people[1] = num_b
        
        people[1], people[ind_a] = people[ind_a], people[1]
        a = minimum_swaps(people[2:])

        people[1], people[ind_a] = people[ind_a], people[1]

        people[0], people[ind_b] = people[ind_b], people[0]
        b = minimum_swaps(people[2:])
        return 1 + min(a, b)