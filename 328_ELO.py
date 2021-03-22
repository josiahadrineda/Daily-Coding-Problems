# https://www.geeksforgeeks.org/elo-rating-algorithm/

class ELO:
    init_score = 400
    k = 30

    def __init__(self):
        self.scores = {}

    def add_player(self, name):
        self.scores[name] = ELO.init_score

    def set_score(self, p1, p2, d):
        """Computes the ELO between two players P1 and P2 depending on the win state D.
        D is either 1 (p1 wins against p2) or -1 (p1 loses against p2).
        """
        assert p1 in self.scores, 'WINNER must be on the scoreboard.'
        assert p2 in self.scores, 'LOSER must be on the scoreboard.'
        assert d in [1, -1], 'D must be valid.'

        s1, s2 = self.scores[p1], self.scores[p2]
        p1, p2 = self._prob(s1, s2), self._prob(s2, s1)

        if d:
            s1 += ELO.k * (1 - p1)
            s2 += ELO.k * -p2
        else:
            s1 += ELO.k * -p1
            s2 += ELO.k * (1 - p2)

        self.scores[p1] = s1
        self.scores[p2] = s2


    def _prob(s1, s2):
        return 1 / (1 + 10**((s1 - s2) / 400))