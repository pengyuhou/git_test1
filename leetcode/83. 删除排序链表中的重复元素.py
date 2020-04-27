# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# [1,1,2,3,3]
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        while cur:
            if cur.val == pre.val:
                cur=cur.next
                if not cur:
                    pre.next=cur
            else:
                pre.next=cur
                cur = cur.next
                pre=pre.next
        return head

















