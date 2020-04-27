# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lx_ = ListNode(-1)
        lx = lx_
        while l1 and l2:
            if l1.val < l2.val:
                lx.next = l1
                l1 = l1.next
            else:
                lx.next = l2
                l2=l2.next
            lx = lx.next
        if l1:
            lx.next = l1
        else:
            lx.next = l2
        return lx_.next








