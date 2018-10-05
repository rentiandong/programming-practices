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


class __Party:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def __le__(self, other):
        return self.num < other.num


def __majority(party, total):
    return party.num() > total / 2


def senate_evacuate(s):
    """
    We will always sequentially remove 2 people from the largest senate, if this
    leaves one party in majority, remove 1 each from the top 2 majority parties

    :param s: a dictionary of the form {'A': #senates, 'B': #senates, ...}
    :return: a list of instructions that looks like ['AB', 'AB', 'AC', 'B', ...]
    """

    parties = [__Party(i, s[i]) for i in s]
    total = sum([s[i] for i in s])
    heapify(parties)
    instructions = []

    while total > 0:

        # edge case of {'A': 1, 'B': 1, 'C': 1} we are forced to evacuate just 1 at this round
        if len(parties) == 3 and total == 3:
            p = heappop(parties)
            total -= 1
            instructions.append(p.name)
            continue

        # get top 2 largest parties
        # there should not be 1 party left at any time as
        # that makes them absolutely majority
        top_1 = heappop(parties)
        top_2 = heappop(parties)

        # evacuate 1 from largest party
        step = top_1.name
        total -= 1

        # if that makes second largest majority, or largest has nothing left
        if __majority(top_2, total) or top_1.num == 0:
            top_2.evacuate()
            step += top_2.name
        else:
            top_1.evacuate()
            step += top_1.name
        total -= 1

        instructions.append(step)

        # put the parties back
        heappush(parties, top_1)
        heappush(parties, top_2)

    return instructions
