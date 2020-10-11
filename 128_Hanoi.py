def hanoi(n):
    """Given N number of discs, returns the steps
    in which to solve the Tower of Hanoi puzzle.

    >>> hanoi(3)
    Move 1 to 3
    Move 1 to 2
    Move 3 to 2
    Move 1 to 3
    Move 2 to 1
    Move 2 to 3
    Move 1 to 3
    """
    def print_step(f, t):
        print(f'Move {f} to {t}')

    def steps(n, f=1, t=3):
        if n:
            v = 6 - f - t
            steps(n-1, f, v)
            print_step(f, t)
            steps(n-1, v, t)

    return steps(n)