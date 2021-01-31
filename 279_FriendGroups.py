def num_friend_groups(friends):
    """A classroom consists of N students, whose friendships can be represented as an
    adjacency list FRIENDS. Each student can be placed in a friend group, which can be
    defined as the transitive closure of said student's friendship relations. Computes
    the number of friend groups that can be found in FRIENDS.

    **Note: FRIENDS is guaranteed to be a valid adjacency list. Also assume that
    FRIENDS is labelled from 0 ... N-1**

    >>> friends = {
    ...     0: [1, 2],
    ...     1: [0, 5],
    ...     2: [0],
    ...     3: [6],
    ...     4: [],
    ...     5: [1],
    ...     6: [3]
    ... }
    >>> num_friend_groups(friends)
    3
    """
    assert friends, 'FRIENDS cannot be an empty dictionary.'

    def dfs(i):
        nonlocal fg
        fg.add(i)
        for neighbor in friends[i]:
            if neighbor not in fg:
                dfs(neighbor)

    friend_groups = set()
    for k in friends.keys():
        fg = set()
        dfs(k)
        friend_groups.add(tuple(sorted(fg)))
    return len(friend_groups)