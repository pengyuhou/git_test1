# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        cur1 = head
        left = []
        right = []
        while cur1:
            v = cur1.val
            if v<x:
                left.append(v)
            else:
                right.append(v)
            cur1 = cur1.next
        a = ListNode(-1)
        ret = left+right
        tmp = a
        while left:
            a.next = ListNode(ret.pop())
        return tmp.next



















