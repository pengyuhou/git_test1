# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 1->2->3->4->5->NULL
# 5->4->3->2->1->NULL
class Solution:
    def reverseList(self, head):
        pre=None
        cur=head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre










