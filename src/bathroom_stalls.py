"""
Google Code Jam qulification round, 2017

A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently
occupied by the bathroom guards. The other N stalls are for users. Whenever someone enters the bathroom, they try to
choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For
each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the
closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest
closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it;
otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls,
they choose the leftmost stall among those. K people are about to enter the bathroom; each one will choose their
stall before the next arrives. Nobody will ever leave. When the last person chooses their stall S, what will the
values of max(LS, RS) and min(LS, RS) be?
"""


from queue import Queue


class Stall:
    def __init__(self, ls, rs, n):
        self.ls = ls
        self.rs = rs
        self.__n = n

    def __lt__(self, other):
        if min(self.ls, self.rs) != min(other.ls, other.rs):
            return min(self.ls, self.rs) < min(other.ls, other.rs)
        else:
            if max(self.ls, self.rs) != max(other.ls, other.rs):
                return max(self.ls, self.rs) > max(other.ls, other.rs)
            else:
                return self.__n > other.__n


def calc_space(n, k):
    """
    :param n: total number of stalls
    :param k: total number of people about to enter
    :return: max(Ls, Rs) and min(Ls, Rs) when everybody entered
    """

    # edge cases of k == n:
    if k >= n or n <= 2 or k == 0:
        return 0, 0

    # let range of stalls be (a, b) where a and b are emtpy
    queue = Queue()
    queue.put((0, n - 1))
    last_stall = Stall(0, 0, -1)

    for i in range(0, k):

        # determine the next stall position
        start, end = queue.get()
        if (start + end) % 2 == 0:
            loc = (start + end) / 2
            last_stall = Stall(loc - start, end - loc, loc)
        else:
            loc_1 = (start + end) // 2
            loc_2 = loc_1 + 1
            stall_1 = Stall(loc_1 - start, end - loc_1, loc_1)
            stall_2 = Stall(loc_2 - start, end - loc_2, loc_2)
            # break ties between stall 1 and stall 2, one has to be larger,
            # since eventually tie is broken by position of stall, which is
            # unique
            if stall_1 > stall_2:
                loc = loc_1
                last_stall = stall_1
            else:
                loc = loc_2
                last_stall = stall_2

        # update empty sequence of stalls
        left = start, loc - 1
        right = loc + 1, end
        left_size = loc - 1 - start
        right_size = end - loc - 1
        if right_size > left_size:
            if right_size >= 0 and queue.qsize() < k - i:
                queue.put(right)
            if left_size >= 0 and queue.qsize() < k - i:
                queue.put(left)
        else:
            if left_size >= 0 and queue.qsize() < k - i:
                queue.put(left)
            if right_size >= 0 and queue.qsize() < k - i:
                queue.put(right)

    return max(last_stall.ls, last_stall.rs), min(last_stall.ls, last_stall.rs)
