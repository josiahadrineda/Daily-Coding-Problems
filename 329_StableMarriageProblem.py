# Gate-Shapley Algorithm
# https://www.geeksforgeeks.org/stable-marriage-problem/

def stable_marriage_problem(men, women):
    """The stable marriage problem is defined as follows:

    Suppose you have N men and N women, and each person has ranked their prospective opposite-sex
    partners in order of preference. The stable marriage problem seeks to match all men and women
    such that no two people of opposite sex would rather be with each other than with their
    current partners.

    >>> men = {
    ...     'Alex': ['Dani', 'Bonnie', 'Carla', 'Anita'],
    ...     'Bob': ['Bonnie', 'Anita', 'Carla', 'Dani'],
    ...     'Chris': ['Anita', 'Bonnie', 'Carla', 'Dani'],
    ...     'David': ['Anita', 'Bonnie', 'Carla', 'Dani']
    ... }
    >>> women = {
    ...     'Anita': ['Alex', 'Bob', 'Chris', 'David'],
    ...     'Bonnie': ['Alex', 'Bob', 'Chris', 'David'],
    ...     'Carla': ['Alex', 'Bob', 'Chris', 'David'],
    ...     'Dani': ['Alex', 'Bob', 'Chris', 'David']
    ... }
    >>> sorted(stable_marriage_problem(men, women))
    [('Alex', 'Dani'), ('Bob', 'Bonnie'), ('Chris', 'Anita'), ('David', 'Carla')]
    """
    assert men, 'MEN cannot be an empty dictionary.'
    assert women, 'WOMEN cannit be an empty dictionary.'

    m, w = list(men), list(women)
    res = {}
    while m:
        x = m.pop(0)
        pref = men[x]
        for p in pref:
            if p in w:
                res[p] = x
                w.remove(p)
                break
            else:
                y = res[p]
                if women[p].index(x) < women[p].index(y):
                    res[p] = x
                    m.append(y)
                    break
    return [(m, w) for w,m in res.items()]