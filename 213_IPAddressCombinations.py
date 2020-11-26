def ip_address_combos(digits):
    """Given a string of digits DIGITS, generates all possible valid
    IP address combinations.

    >>> ip_address_combos('2542540123')
    ['254.25.40.123', '254.254.0.123']
    >>> ip_address_combos('100100110')
    ['10.0.100.110', '100.10.0.110', '100.100.1.10', '100.100.11.0']
    """
    assert digits, 'DIGITS cannot be an empty string.'

    def combos_recur(digits, curr):
        if len(curr) > 4 or (len(curr) < 4 and not digits):
            return
        elif len(curr) == 4 and not digits:
            res.add('.'.join(curr))
        else:
            for i in range(1, 4):
                s = digits[:i]
                if s and \
                    ((s[0] == '0' and len(s) == 1) or \
                    (s[0] != '0' and (0 <= int(s) <= 255))):
                    curr.append(s)
                    combos_recur(digits[i:], curr)
                    curr.pop()

    res = set()
    combos_recur(digits, [])
    return sorted(list(res))