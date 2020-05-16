# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        cur = head
        res = []
        stack = []
        while cur:
            stack.append(cur.val)
            if len(stack) == k:
                res += stack[::-1]
                stack.clear()
            cur = cur.next
        if stack:
            res += stack
        a = ListNode(-1)
        tmp = a
        while res:
            a.next = ListNode(res.pop(0))
            a = a.next
        return tmp.next
