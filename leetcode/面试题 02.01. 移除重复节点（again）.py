# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        from collections import defaultdict
        d = defaultdict(int)
        pre = ListNode(-1)
        cur = head
        pre.next = cur
        tmp = head
        while cur:
            d[cur.val] += 1
            if d[cur.val] > 1:
                d[cur.val] -= 1
                cur = cur.next
                pre.next = cur
            else:
                cur = cur.next
                pre = pre.next
        return tmp
