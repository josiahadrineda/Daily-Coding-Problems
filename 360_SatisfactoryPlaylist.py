class Node:
    def __init__(self, val):
        self.val = val
        self.children = set()

def satisfactory_playlist(favorite_songs):
    """Given a list of lists FAVORITE_SONGS (abbreviated to FS), where FS[i] is the
    ordering of the ith person's favorite songs (the most favorite at index 0 and the
    least favorite at len(FS[i]) - 1), creates a playlist that satisfies everyone's
    tastes. If no valid playlist can be created, returns an empty list.

    **Note: Every song is guaranteed to be a positive integer.**

    >>> favorite_songs = [[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]]
    >>> satisfactory_playlist(favorite_songs)
    [2, 1, 6, 7, 3, 9, 5]
    >>> favorite_songs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> satisfactory_playlist(favorite_songs)
    [7, 8, 9, 4, 5, 6, 1, 2, 3]
    >>> favorite_songs = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    >>> satisfactory_playlist(favorite_songs)
    []
    """
    assert favorite_songs, 'FAVORITE_SONGS cannot be an empty list.'

    """
    General Idea:
    1. Create a DAG from FAVORITE_SONGS
    2. Return a topological sort of the DAG
    """

    def connect(nodes, fav):
        for i in range(len(fav) - 1):
            v1, v2 = fav[i], fav[i + 1]
            nodes[v1].children.add(nodes[v2])

    def has_cycle(vals, nodes):
        def cycle_recur(curr, rec_stack):
            if curr.val in rec_stack:
                return True
            elif curr.val in visited:
                return False

            visited.add(curr.val)
            
            rec_stack.add(curr.val)
            for c in curr.children:
                if cycle_recur(c, rec_stack):
                    return True
            rec_stack.remove(curr.val)

        vals, visited = set(vals), set()
        while vals:
            curr_val = vals.pop()
            if cycle_recur(nodes[curr_val], set()):
                return True
        return False

    def topological_sort(vals, nodes):
        def top_sort_recur(curr):
            if curr.val in visited:
                return

            visited.add(curr.val)
            for c in curr.children:
                top_sort_recur(c)
            top_sort.append(curr.val)

        top_sort, visited = [], set()
        while vals:
            curr_val = vals.pop()
            top_sort_recur(nodes[curr_val])
        return top_sort[::-1]

    vals, nodes = set(), {}
    for fav in favorite_songs:
        for s in fav:
            vals.add(s)
            nodes[s] = Node(s)

    for fav in favorite_songs:
        connect(nodes, fav)

    if has_cycle(vals, nodes):
        return []
    return topological_sort(vals, nodes)