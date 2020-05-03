# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        cur1 = head
        ret = []
        while cur1:
            ret.append(cur1.val)
            cur1 = cur1.next
        res = ret[:m-1]+ret[m-1:n][::-1]+ret[n:]
        a = ListNode(-1)
        tmp = a
        while res:
            a.next = ListNode(res.pop(0))
            a =a.next
        return tmp.next









