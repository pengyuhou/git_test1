# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
"""

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur:
            cur=cur.next
            count += 1
        cur1=head
        for i in range(count-k):
            cur1=cur1.next
        return cur1














