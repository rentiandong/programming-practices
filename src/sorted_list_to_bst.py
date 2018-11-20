from data_structures.binary_tree import TreeNode


def __arr2bst(arr, start, end):
    # base case, no elements left
    if end < start:
        return None
    mid = (start + end) // 2
    root = TreeNode(arr[mid])
    root.left = __arr2bst(arr, start, mid - 1)
    root.right = __arr2bst(arr, mid + 1, end)
    return root


def sorted_list_to_bst(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return __arr2bst(arr, 0, len(arr) - 1)
