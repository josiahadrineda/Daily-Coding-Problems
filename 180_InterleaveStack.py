# https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_180.py
# DCP didn't email me today's problem for some reason...

def interleave_stack(stack, queue):
    """Given a STACK and a QUEUE, transforms the STACK's contents
    into an interleaved STACK, where the elements from left to right
    are s[0], s[len(s)-1], s[1], s[len(s)-2] ...

    >>> from queue import Queue
    >>> stack = [1, 2, 3, 4, 5]
    >>> interleave_stack(stack, Queue())
    >>> stack
    [1, 5, 2, 4, 3]
    >>> stack = [1, 2, 3, 4]
    >>> interleave_stack(stack, Queue())
    >>> stack
    [1, 4, 2, 3]
    """
    assert stack, 'Cannot interleave an empty STACK.'

    def interleave_stack_recur(stack, queue, ind=1):
        for _ in range(len(stack) - ind):
            queue.put(stack.pop())

        while queue.qsize():
            stack.append(queue.get())

        if len(stack) - ind > 1:
            interleave_stack_recur(stack, queue, ind + 1)

    interleave_stack_recur(stack, queue)