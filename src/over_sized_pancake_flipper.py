# Google Coding Jam 2017 Qualification Round
# 
# suppose total n cakes, must flip k at a time
#
# we can solve by using a greedy algorithm: iterate from left
# to right, if the current pancake is False, we flip it and the
# subsequent k - 1 cakes using the over-sized flipper. When we
# get to index n - k (no more can be flipped), check if all cakes
# have their happy side up.
#
# In other words we are pushing all sad cakes to the right, if
# if we are left with k cakes of the same face at the end, then
# it will be solvable.


def __solved(arr):
    for i in arr:
        if not i:
            return False
    return True


def num_flips(arr, k):
    c = 0
    for i in range(0, len(arr)):
        if len(arr) - i < k:
            if __solved(arr):
                return c
            else:
                return 'Unsolvable'
        if not arr[i]:
            c += 1
            for j in range(i, i + k):
                arr[j] = not arr[j]
