"""
Given two arrays of length m and n with digits 0-9 representing two numbers. 
Create the maximum number of length k <= m + n from digits of the two. The 
relative order of the digits from the same array must be preserved. Return an 
array of the k digits.

Example 1:
Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]

Example 2:
Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]

Example 3:
Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
"""


def num2arr(num):
    return [int(i) for i in str(num)]


def max_rec(nums1, nums2, k, pos1, pos2, seq, mem):

    # base case 0, if sub problem already solved
    if (pos1, pos2, seq) in mem:
        return mem[(pos1, pos2, seq)]

    # base case 1, k digits all filled
    if seq is not None:
        if len(str(seq)) == k:
            return seq

    # base case 2, depleted both nums arr but did not have k digits
    seq_len = len(str(seq))
    if seq is None:
        seq_len = 0
    if (k - seq_len) > (len(nums1) - pos1 + len(nums2) - pos2):
        return -1

    ans = []
    if seq is None:
        seq = 0

    res_1 = -1
    res_3 = -1
    if pos1 < len(nums1):
        # recursive case 1, use next digit in nums1
        seq = seq * 10 + nums1[pos1]
        res_1 = max_rec(nums1, nums2, k, pos1 + 1, pos2, seq, mem)
        seq = (seq - nums1[pos1]) // 10
        # recursive case 3, skip next digit in nums1
        res_3 = max_rec(nums1, nums2, k, pos1 + 1, pos2, seq, mem)
    ans.append(res_1)
    ans.append(res_3)

    res_2 = -1
    res_4 = -1
    if pos2 < len(nums2):
        # recursive case 2, use next digit in nums2
        seq = seq * 10 + nums2[pos2]
        res_2 = max_rec(nums1, nums2, k, pos1, pos2 + 1, seq, mem)
        seq = (seq - nums2[pos2]) // 10
        # recursive case 4, skip next digit in nums2
        res_4 = max_rec(nums1, nums2, k, pos1, pos2 + 1, seq, mem)
    ans.append(res_2)
    ans.append(res_4)

    mem[(pos1, pos2, seq)] = max(ans)
    return mem[(pos1, pos2, seq)]


def max_number(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[int]
    """
    return num2arr(max_rec(nums1, nums2, k, 0, 0, None, {}))
