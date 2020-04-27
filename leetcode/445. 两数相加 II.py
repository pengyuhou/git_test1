# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(str(l1.val))
            l1 = l1.next
        while l2:
            stack2.append(str(l2.val))
            l2 = l2.next
        res = list(str(int(''.join(stack1)) + int(''.join(stack2))))
        pre = ListNode(-1)
        tmp = pre
        while res:
            pre.next = ListNode(res.pop(0))
            pre = pre.next
        return tmp.next




