class SubscriberCounter:
    """A data structure for handling hourly subscriber count.

    **Note**: Assume that start < end and start and end indices will fall
    within the range of [1, 24].

    >>> sc = SubscriberCounter()
    >>> for i in range(1, 25):
    ...     sc.update(i, i)
    >>> sc.query(1, 10)
    55
    """

    def __init__(self):
        self.analytics = [0] * 24

    def update(self, hour, value):
        self.analytics[hour - 1] += value

    def query(self, start, end):
        return sum(self.analytics[start - 1: end])