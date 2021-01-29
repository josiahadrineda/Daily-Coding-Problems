def valid_encoding(byte_vals):
    """Given a list of positive integers representing byte values BYTE_VALS, returns
    whether or not it is a valid UTF-8 encoding.

    A character in UTF-8 can be from 1-4 bytes long, subjected to the following rules:
        1. For a 1-byte character, the first bit is a 0, followed by its unicode code.
        2. For an n-byte character, the first n bits are all 1s, the (n+1)th bit is 0,
        followed by n-1 bytes with the most significant 2 bits being 10.

    >>> valid_encoding([197, 130, 1])
    True
    >>> valid_encoding([235, 140, 4])
    False
    """
    assert byte_vals, 'BYTE_VALS cannot be an empty list.'
    
    if any([bv > 247 for bv in byte_vals]):
        return False

    num_bytes = 0
    for bv in byte_vals:
        bv = bin(bv)[2:]
        bv = '0' * (8 - len(bv)) + bv

        if num_bytes:
            if bv[:2] != '10':
                return False
            num_bytes -= 1
        else:
            if bv[0] == '0':
                num_bytes = 0
            else:
                while bv[num_bytes] == '1':
                    num_bytes += 1
                num_bytes -= 1
    return not num_bytes