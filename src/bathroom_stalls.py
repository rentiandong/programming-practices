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
        self.__ls = ls
        self.__rs = rs
        self.__n = n

    def __lt__(self, other):
        if min(self.__ls, self.__rs) != min(other.__ls, other.__rs):
            return min(self.__ls, self.__rs) < min(other.__ls, other.__rs)
        else:
            if max(self.__ls, self.__rs) != max(other.__ls, other.__rs):
                return max(self.__ls, self.__rs) > max(other.__ls, other.__rs)
            else:
                return self.__n > other.__n


def calc_space(n, k):
    """
    :param n: total number of stalls
    :param k: total number of people about to enter
    :return: max(Ls, Rs) and min(Ls, Rs) when everybody entered
    """

    # edge case of k == n:
    if k >= n:
        return 0, 0

    if n <= 2:
        return 0, 0

    # let range of stalls be (a, b) where a and b are emtpy
    queue = Queue()
    queue.put((1, n - 2))

    for i in range(0, k):

        # determine the next stall position
        start, end = queue.get()
        if (start + end) % 2 == 0:
            loc = (start + end) / 2
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
            else:
                loc = loc_2

        # update empty sequence of stalls
        if loc - 1 >= start:
            queue.put((start, loc - 1))
        if end >= loc + 1:
            queue.put((loc + 1, end))

    # after everybody gets in their stalls, look through all
    # empty spaces stored in queue and find desired spacing sizes
    largest = 0
    smallest = n
    while not queue.empty():
        start, end = queue.get()
        loc = (start + end) / 2  # odd / even does not matter here
        larger = max(loc - start, end - loc)
        smaller = min(loc - start, end - loc)
        if larger > largest:
            largest = larger
        if smaller < smallest:
            smallest = smaller

    return largest, smallest
