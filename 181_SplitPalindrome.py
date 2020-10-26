def split_palindrome(s):
    """Given a string S, splits S into as few strings as possible
    such that each string is a palindrome.

    >>> split_palindrome('racecarannakayak')
    ['racecar', 'anna', 'kayak']
    >>> split_palindrome('abc')
    ['a', 'b', 'c']
    """
    assert s, 'S cannot be an empty string.'

    def split_palindrome_recur(s, curr, pals):
        if not s and not curr:
            return pals
        elif not s:
            return pals + list(curr)

        curr, s = curr + s[0], s[1:]
        if is_palindrome(curr):
            take_curr = split_palindrome_recur(s, '', pals + [curr])
            leave_curr = split_palindrome_recur(s, curr, pals)
            return min(take_curr, leave_curr, key=len)
        else:
            return split_palindrome_recur(s, curr, pals) 

    def is_palindrome(s):
        return s == s[::-1]

    return split_palindrome_recur(s, '', [])