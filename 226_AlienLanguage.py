from collections import defaultdict

def order_of_letters(words):
    """Given a sorted list of words WORDS in a language you've never seen before,
    returns the correct order of letters in this language.

    >>> order_of_letters(['caa', 'aaa', 'aab'])
    ['c', 'a', 'b']
    >>> order_of_letters(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'])
    ['x', 'z', 'w', 'y']
    """
    assert words, 'WORDS cannot be an empty list.'

    graph = defaultdict(list)
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                graph[c1].append(c2)
                break

    letters = list(set(list(''.join(words))))
    for l in letters:
        if l not in graph:
            graph[l] = []

    return topological_sort(graph, letters)

def topological_sort(graph, letters):
    def top_sort_recur(curr, visited, stack):
        visited[curr] = True
        for c in graph[curr]:
            if not visited[c]:
                top_sort_recur(c, visited, stack)
        stack.append(curr)

    visited = {l: False for l in letters}
    stack = []
    for c in graph.keys():
        top_sort_recur(c, visited, stack)
    return stack[-len(letters):]