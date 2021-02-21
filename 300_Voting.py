class VotingMachine:
    """
    A class representing a basic voting machine. Supports ranking and fraud detection.

    >>> vm = VotingMachine(['a', 'b', 'c', 'd', 'e'])
    >>> vm.vote(1, 'a')
    >>> vm.vote(2, 'a')
    >>> vm.vote(3, 'c')
    >>> vm.vote(4, 'b')
    >>> vm.vote(5, 'c')
    >>> vm.vote(6, 'a')
    >>> vm.vote(7, 'e')
    >>> vm.vote(7, 'd')
    'FraudulenceException: 7 has already voted.'
    >>> vm.rank()
    ['a', 'c', 'b', 'e', 'd']
    """

    def __init__(self, candidates):
        self.voters = set()
        self.candidates = {}
        for cand in candidates:
            self.candidates[cand] = 0

    def vote(self, voter_id, candidate_id):
        if voter_id in self.voters:
            return f"FraudulenceException: {voter_id} has already voted."

        self.voters.add(voter_id)
        self.candidates[candidate_id] += 1

    def rank(self):
        return [cand for cand, votes in sorted(self.candidates.items(), key=lambda x: x[1], reverse=True)]