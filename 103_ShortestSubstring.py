def shortest_substring(s, chars):
    """
    Returns the shortest substring containing all chars.
    Returns None if no substring is present.

    >>> shortest_substring('figehaeci', ['a', 'e', 'i'])
    'aeci'

    >>> shortest_substring('figehaeci', ['a', 'e', 'i', 'o', 'u'])

    """

    if not chars:
        if not s:
            return ''
        else:
            return s[0]
    elif not s:
        return None

    if not validate_s_and_chars(s, chars):
        return None

    # Brute force
    """res = ''
    min_len = float('inf')
    for j in range(len(chars), len(s)+1):
        for i in range(j-2):
            substr = s[i:j]
            cnt = 0
            for c in chars:
                if c in substr:
                    cnt += 1
            
            if cnt == len(chars):
                if len(substr) < min_len:
                    min_len = len(substr)
                    res = substr
    return res if res else None"""

    # Modified binary search
    """res = ''
    min_len = float('inf')
    window_size = len(s) // 2
    visited_window_sizes = set()
    while len(chars) <= window_size <= len(s):
        if window_size in visited_window_sizes:
            break

        temp = find_substring(s, chars, window_size)
        if temp:
            visited_window_sizes.add(window_size)
            window_size -= 1
            
            if len(temp) < min_len:
                min_len = len(temp)
                res = temp
        else:
            window_size += 1
    return res if res else None"""

    # Sliding window (GeeksForGeeks), LEARN AND IMPROVE UPON THIS
    # Maybe experiment with multiple while loops in the future
    NUM_CHARS = 256

    min_len = float('inf')
    start_ind = 0

    s_map = [0] * NUM_CHARS
    chars_map = [0] * NUM_CHARS
    chars_map = map_chars(chars_map, chars)

    cnt = 0
    start = 0
    for i in range(len(s)):
        s_map[ord(s[i])] += 1
        if s_map[ord(s[i])] != 0 and \
            chars_map[ord(s[i])] != 0 and \
            s_map[ord(s[i])] <= chars_map[ord(s[i])]:
            cnt += 1

        if cnt == len(chars):
            while chars_map[ord(s[start])] == 0 or \
                s_map[ord(s[start])] > chars_map[ord(s[start])]:
                if s_map[ord(s[start])] > chars_map[ord(s[start])]:
                    s_map[ord(s[start])] -= 1
                start += 1

            window_len = i - start + 1
            if window_len < min_len:
                min_len = window_len
                start_ind = start
    return s[start_ind:start_ind + min_len]

def validate_s_and_chars(s, chars):
    s_set = set(s)
    for c in chars:
        if c not in s_set:
            return False
    return True

def find_substring(s, chars, window_size):
    i, j = 0, window_size
    while j <= len(s):
        substr = s[i:j]
        cnt = 0
        for c in chars:
            if c in substr:
                cnt += 1
        
        if cnt == len(chars):
            return substr

        i += 1
        j += 1
    return ''

def map_chars(chars_map, chars):
    for c in chars:
        chars_map[ord(c)] += 1
    return chars_map