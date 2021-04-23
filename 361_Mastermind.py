# https://github.com/NathanDuran/Mastermind-Five-Guess-Algorithm#:~:text=Five%2DGuess%2DAlgorithm-,Donal%20Knuth's%20five%20guess%20algorithm%20for%20solving%20the%20game%20Mastermind,the%20number%20of%20possible%20patterns.

DIGITS = '0123456789'

def mastermind(guesses):
    """Mastermind is a two-player game in which the first player attempts to guess the
    secret code of the second. In this version, the code may be any six-digit number
    with all distinct digits.

    Each turn the first player guesses some number, and the second player responds by
    saying how many digits in this number correctly matched their location in the
    secret code. For example, if the secret code were 123456, then a guess of 175286
    would score two, since 1 and 6 were correctly placed.

    Given a sequence of guesses and their scores, determines whether there exists some
    secret code that could have produced them. If true, returns a valid code. If
    false, returns an empty string.

    **Note: Assumes that all guesses are strings of equal length.**

    >>> mastermind({'175286': 2, '293416': 3, '654321': 0})
    '013486'
    >>> mastermind({'123456': 4, '345678': 4, '567890': 4})
    ''
    """
    assert guesses, 'GUESSES cannot be an empty dictionary.'

    def is_valid(guess):
        for g, s in guesses_list:
            score = sum(c1 == c2 for c1,c2 in zip(guess, g))
            if score != s:
                return False
        return True

    def backtrack(digits, curr):
        if len(curr) == n:
            if is_valid(curr):
                return curr
            return ''
        else:
            for i,d in enumerate(digits):
                cand = backtrack(digits[:i] + digits[i + 1:], curr + d)
                if cand:
                    return cand
            return ''

    guesses_list = list(guesses.items())
    n = len(guesses_list[0][0])
    return backtrack(list(DIGITS), '')