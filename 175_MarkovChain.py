import random
import bisect

def markov_chain(start, num_steps, probs):
    """Given a starting state START, the number of steps to run the Markov Chain NUM_STEPS,
    and a list of transition probabilities PROBS, computes the number of times each state
    is visited (one possibility).

    >>> probs = [
    ...     ('a', 'a', 0.9),
    ...     ('a', 'b', 0.075),
    ...     ('a', 'c', 0.025),
    ...     ('b', 'a', 0.15),
    ...     ('b', 'b', 0.8),
    ...     ('b', 'c', 0.05),
    ...     ('c', 'a', 0.25),
    ...     ('c', 'b', 0.25),
    ...     ('c', 'c', 0.5)
    ... ]
    >>> state_count = markov_chain('a', 5000, probs)
    >>> assert state_count['a'] > state_count['b'] > state_count['c']
    """
    assert start in [p[0] for p in probs] or start in [p[1] for p in probs], 'Not a valid START state.'
    assert num_steps > 0, 'NUM_STEPS must be a positive integer.'

    states = list(sorted(set([p[0] for p in probs])))
    cum_probs = {}
    tot, curr = 0, -1
    for i in range(len(probs)):
        if i % len(states) == 0:
            tot, curr = 0, curr + 1
        tot += probs[i][2]
        if not cum_probs.get(states[curr]):
            cum_probs[states[curr]] = []
        cum_probs[states[curr]].append(tot)

    probs_dict = {}
    for s1 in states:
        for ind, s2 in enumerate(states):
            probs_dict[(s1, cum_probs[s1][ind])] = s2
            i += 1

    state_count = {}
    curr = start
    for _ in range(num_steps):
        rand = random.random()
        ind = bisect.bisect_left(cum_probs[curr], rand)
        curr = probs_dict[(curr, cum_probs[curr][ind])]
        if not state_count.get(curr):
            state_count[curr] = 0
        state_count[curr] += 1
    
    return state_count