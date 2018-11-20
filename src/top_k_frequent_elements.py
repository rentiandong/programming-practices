from bisect import insort


class Solution:
    def top_k_frequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        class Counter:
            # noinspection PyShadowingNames
            def __init__(self, num, count):
                self.num = num
                self.count = count

            def __lt__(self, other):
                return self.count > other.count

            def __repr__(self):
                return str(self.num)

        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        arr = []
        for i in count:
            c = Counter(i, count[i])
            insort(arr, c)
        return arr[:k]
