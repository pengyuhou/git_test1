# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        ret1 = []
        ret2 = []
        count = 0
        while cur:
            if count % 2:
                ret2.append(cur.val)
            else:
                ret1.append(cur.val)
            count += 1
            cur = cur.next
        ret = ret1+ret2
        a = ListNode(-1)
        tmp = a
        while ret:
            a.next = ListNode(ret.pop(0))
            a = a.next
        return tmp.next