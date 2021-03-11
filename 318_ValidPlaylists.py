"""Note: This will TLE on large (~40-100) input sizes

You could reimplement this with the recursive relation:
F(m, n, b) = F(m - 1, n - 1, b) * m + F(m, n - 1, b) * max(0, m - b)

Where:
- F(m, n, b) = # valid playlists of length N with M songs and a buffer of length B
- F(m - 1, n - 1, b) * m = # valid playlists guaranteeing that the last song is UNIQUE
- F(m, n - 1, b) * max(0, m - b) = # valid playlists guaranteeing that the last REUSED
  song is not in B
"""

def valid_playlists(m, n, b):
    """You are going on a road trip, and would like to create a suitable music
    playlist. The trip will require N songs, though you only have M songs downloaded
    (M <= N). A valid playlist should select each song at least once, and guarantee a
    buffer of B songs between repeats. Given positive integers M and N as well as
    nonnegative integer B, determines the number of valid playlists.

    >>> valid_playlists(3, 3, 1)
    6
    >>> valid_playlists(4, 6, 2)
    168
    """
    assert m > 0, 'M must be a positive integer.'
    assert n > 0, 'N must be a positive integer.'
    assert b >= 0, 'B must be a nonnegative integer.'
    assert m <= n, 'M must be less than N.'

    def dfs(m, n, playlist, buffer):
        if not n:
            if is_valid(playlist):
                res.add(playlist)
            return
        
        if len(buffer) > b:
            buffer.pop(0)
        buffer_set = set(buffer)
        for song in range(m):
            if song not in buffer_set:
                dfs(m, n - 1, playlist + tuple([song]), buffer + [song])

    def is_valid(playlist):
        return len(set(playlist)) == m

    res = set()
    dfs(m, n, tuple(), [])
    return len(res)