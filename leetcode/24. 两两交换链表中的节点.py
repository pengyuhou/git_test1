# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cp = ListNode(-1)
        cp.next = head

        pre = head
        cur = head.next
        while cur and pre:

            pre.next = cur.next
            cur.next = pre



        return cp.next
















