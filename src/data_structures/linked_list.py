class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def from_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    tail = head
    for i in range(1, len(arr)):
        tail.next = ListNode(arr[i])
        tail = tail.next
    return head
