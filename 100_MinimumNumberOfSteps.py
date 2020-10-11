def get_min_steps(steps):
    res = 0
    if not steps:
        return res

    for i in range(len(steps)):
        if i == 0:
            res = calculate_distance(res, steps[i])
        else:
            res = calculate_distance(res, steps[i], start=steps[i-1])
    return res

def calculate_distance(res, end, start=(0,0)):
    if start == end:
        return res
    
    sx, sy = start
    ex, ey = end

    if sx == ex:
        # Horizontals
        return res + abs(ey - sy)
    elif sy == ey:
        # Verticals
        return res + abs(ex - sx)
    else:
        # Diagonals
        if sx < ex and sy < ey:
            return calculate_distance(res + 1, end, start=(sx+1, sy+1))
        elif sx > ex and sy < ey:
            return calculate_distance(res + 1, end, start=(sx-1, sy+1))
        elif sx < ex and sy > ey:
            return calculate_distance(res + 1, end, start=(sx+1, sy-1))
        elif sx > ex and sy > ey:
            return calculate_distance(res + 1, end, start=(sx-1, sy-1))

assert get_min_steps([]) == 0
assert get_min_steps([(0, 0)]) == 0
assert get_min_steps([(0, 0), (1, 1), (1, 2)]) == 2
assert get_min_steps([(0, 0), (1, 1), (1, 2), (3, 4)]) == 4
assert get_min_steps([(0, 0), (1, 1), (1, 2), (3, 6)]) == 6
assert get_min_steps([(7,7)]) == 7