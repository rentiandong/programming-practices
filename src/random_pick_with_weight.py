from random import randint


class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        rs = 0
        m = []
        for i in range(0, len(w)):
            rs += w[i]
            m.append((rs, i))
        m.sort(key=lambda x: x[0])
        self.mapping = m
        self.sum = rs

    def pick_index(self):
        """
        :rtype: int
        """
        r = randint(0, self.sum - 1)
        start = 0
        end = len(self.mapping) - 1
        while start <= end:
            mid = int(.5 * (start + end))
            if start == end:
                return self.mapping[mid][1]
            elif self.mapping[mid - 1][0] <= r < self.mapping[mid][0]:
                return self.mapping[mid][1]
            elif r >= self.mapping[mid][0]:
                start = mid + 1
            else:
                end = mid
