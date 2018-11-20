# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_lists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l2 is None:
        return l1
    elif l1 is None:
        return l2
    new_head = None
    new_tail = None
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            temp = l1
            l1 = l1.next
        else:
            temp = l2
            l2 = l2.next
        temp.next = None
        if new_head is None:
            new_head = temp
            new_tail = temp
        else:
            new_tail.next = temp
            new_tail = temp
    remain = l1 if l2 is None else l2
    while remain is not None:
        new_tail.next = remain
        new_tail = remain
        remain = remain.next
        new_tail.next = None
    return new_head
