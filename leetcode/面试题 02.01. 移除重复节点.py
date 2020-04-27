# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# [1, 2, 2]

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre=head
        cur=head.next
        a=[pre.val]
        while cur:
            if cur.val not in a:
                a.append(cur.val)
                cur = cur.next
                pre=pre.next
            else:
                pre.next=cur.next
                cur = cur.next
        return head




