"""
Found on LeetCode

Given a string containing just the characters '(' and ')', find the length of
the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


# check if the given substring is valid
def __check_all(s, start, end):
    left = 0
    right = 0
    for i in range(start, end):
        if left - right > end - i:
            return False
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if right > left:
            return False
    if left != right:
        return False
    return True


def __max_paren(s, start, end, mem):

    # base case 0, if problem already solved
    if (start, end) in mem:
        return mem[(start, end)]

    # base case 1, length < 1, no valid paren
    if end - start < 1:
        return 0, None, None

    # recursive case 1, check if entire string is valid, skip recursive case 2 if so
    if __check_all(s, start, end):
        ans = (end - start), start, end
        mem[(start, end)] = ans
        return ans

    # recursive case 2, break string in every possible location and continue
    # combine if possible
    my_max = 0, None, None
    for i in range(start + 1, end):
        len_l, start_l, end_l = __max_paren(s, start, i, mem)
        len_r, start_r, end_r = __max_paren(s, i, end, mem)
        if start_r == end_l:  # rec case 2.1 can combine
            res = (len_l + len_r), start_l, end_r
        else:  # rec case 2.2 cannot combine, choose larger of len_l and len_r
            if len_l > len_r:
                res = len_l, start_l, end_l
            else:
                res = len_r, start_r, end_r
        # update maximum
        if res[0] > my_max[0]:
            my_max = res

    mem[(start, end)] = my_max
    return my_max


def longest_valid_parentheses(s):
    """
    :type s: str
    :rtype: int
    """
    return __max_paren(s, 0, len(s), {})[0]
