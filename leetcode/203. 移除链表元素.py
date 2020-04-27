# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        if not head.next:
            if head.val!=val:
                return head
            else:
                return None
        cur = head.next
        pre = head
        while cur:
            if cur.val == val:
                pre.next=cur.next
                cur = cur.next
                continue
            cur = cur.next
            pre = pre.next
        if head.val==val:
            return head.next
        else:
            return head



