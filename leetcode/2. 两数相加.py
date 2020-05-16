# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = []
        b = []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        a.reverse()
        b.reverse()
        res = list(str(int(''.join([str(i) for i in a])) + int(''.join([str(j) for j in b]))))
        res.reverse()
        ret = [int(i) for i in res]
        a = ListNode(-1)
        tmp = a
        while ret:
            a.next = ListNode(ret.pop(0))
            a = a.next
        return tmp.next



