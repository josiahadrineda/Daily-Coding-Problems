def dodgeball(students):
    """Given an adjacency list of students' dislikes STUDENTS, attempts to partition
    STUDENTS into two dodgeball teams where every student in both teams are on equal
    terms with one another (not dislike). If not possible, returns False.

    **Note: Each student in STUDENTS should be labeled from 1...N.**

    >>> students = {
    ...     0: [3],
    ...     1: [2],
    ...     2: [1, 4],
    ...     3: [0, 4, 5],
    ...     4: [2, 3],
    ...     5: [3]
    ... }
    >>> dodgeball(students)
    ({0, 1, 4, 5}, {2, 3})
    >>> students[2] = [1, 3, 4]
    >>> students[3] = [0, 4, 5]
    >>> dodgeball(students)
    False
    """
    assert students, 'STUDENTS cannot be an empty dictionary.'

    def partition(student, team):
        teams[team].add(student)
        can_partition = True
        for dislike in students[student]:
            if dislike in teams[team] or not can_partition:
                return False
            other = abs(team - 1)
            if dislike not in teams[other]:
                can_partition = partition(dislike, other)
        return can_partition

    teams = {}
    teams[0], teams[1] = set(), set()

    can_partition = partition(0, 0)
    return can_partition and (teams[0], teams[1])