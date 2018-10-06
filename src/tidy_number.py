"""
Google Code Jam 2017 Practice Round

some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order.
Some examples of this are 8, 123, 555, and 224488. Call these numbers tidy numbers. Numbers that do not have
this property, like 20, 321, 495 and 999990, are not tidy. Find largest tidy number less than N
"""


def tidy_number(n):
    """
    Scan from largest decimal position of n to lowest, at first decimal position
    where digits decrease, return to the previous decimal, set that to 1 less of
    its previous value, and set all subsequent decimal values to 9.

    :param n: largest possible number, as a string
    :return: the largest tidy number smaller than n, as a string
    """

    if len(n) == 1:
        return str(n)

    for i in range(1, len(n)):
        if n[i] < n[i - 1]:  # found decreasing point
            m = n[i]
            j = i - 1
            while j > 0:
                if n[j] <= m:
                    break
                j -= 1
            if j == 0 and n[j] > m:  # handle edge case where turning point is first digit
                res = [str(int(n[0]) - 1)]
                res += ['9' for _ in range(1, len(n))]
            else:
                res = [n[k] for k in range(0, j + 1)]
                res.append(str(int(n[j + 1]) - 1))
                res += ['9' for _ in range(j + 2, len(n))]
            res = ''.join(res)
            if res[0] == '0':
                res = res[1:]
            return res
    return n  # if decreasing point never found, input is already tidy
