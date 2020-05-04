# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ret = []
        cur = head
        while cur:
            if cur not in ret:
                ret.append(cur)
            else:
                return True
            cur = cur.next
        return False





