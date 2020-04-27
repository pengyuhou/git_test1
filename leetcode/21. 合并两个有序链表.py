# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 1->2->4, 1->3->4
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lis_=ListNode(-1)
        lis=lis_

        while l1 and l2:
            if l1.val<l2.val:
                lis.next=l1
                l1=l1.next
            else:
                lis.next=l2
                l2=l2.next
            lis=lis.next
        if not l1:
            lis.next=l2
        else:
            lis.next=l1
        return lis_.next








