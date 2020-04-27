# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# head = [3,2,0,-4], pos = 1


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur = head
        while cur:
            if not cur.val:
                return True
            cur.val = None
            cur = cur.next
        return False




