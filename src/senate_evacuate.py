"""
From Google Code Jam Practice Session 2018

A small fire started in the senate room, and it needs to be evacuated! There are some senators in the senate room,
each of whom belongs to of one of N political parties. Those parties are named after the first N (uppercase) letters
of the English alphabet. The emergency door is wide enough for up to two senators, so in each step of the evacuation,
you may choose to remove either one or two senators from the room. The senate rules indicate the senators in the room
may vote on any bill at any time, even in the middle of an evacuation! So, the senators must be evacuated in a way
that ensures that no party ever has an absolute majority. That is, it can never be the case after any evacuation step
that more than half of the senators in the senate room belong to the same party. Can you construct an evacuation
plan? The senate is counting on you!
"""
from heapq import heapify, heappop, heappush


class EvacPlan:

    """
    If total number of people is odd, pop 1 from the largest party, make that
    the first instruction (just evacuate 1 people in that round)

    Then for the remaining even number of people We will always pop from the
    current largest party. Then group instructions into pairs of two to minimize
    rounds and avoid breaking in situations where only two parties left and their
    numbers are equal.
    """

    def __init__(self, s):
        """
        :param s: a dictionary of the form {'A': #senates, 'B': #senates, ...}
        """
        class __Party:  # simple object to represent a party
            def __init__(self, name, num):
                self.name = name
                self.num = num

            def __lt__(self, other):
                return self.num > other.num  # reverse to turn min heap to max heap

        self.__parties = [__Party(i, s[i]) for i in s]
        self.__total = sum([s[i] for i in s])
        heapify(self.__parties)
        self.plan = None
        self.__group = ''
        self.__make_plan()

    def __evac_largest(self):
        largest_party = heappop(self.__parties)
        largest_party.num -= 1
        self.__total -= 1
        self.__group += largest_party.name
        if len(self.__group) == 2:
            self.plan.append(self.__group)
            self.__group = ''
        if largest_party.num > 0:
            heappush(self.__parties, largest_party)

    def __make_plan(self):

        if self.plan is not None:
            return self.plan
        else:
            self.plan = []

        # make total people even
        if self.__total % 2 == 1:
            self.__evac_largest()
            self.plan.append(self.__group)
            self.__group = ''

        while self.__total > 0:
            self.__evac_largest()

        if len(self.__group) == 1:
            self.plan.append(self.__group)
