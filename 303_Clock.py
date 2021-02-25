def angle(time):
    """Given a string TIME in the format "hh:mm", determines, to the nearest degree,
    the angle between the hour and the minute hands.

    >>> angle("12:30")
    165
    >>> angle("03:30")
    75
    """
    assert time, 'TIME cannot be an empty string.'

    h, m = int(time[:2]), int(time[3:])
    
    m *= 6
    h = round((h * 30) + (m / 12))
    h %= 360

    angle = abs(h - m)
    return min(angle, 360 - angle)