# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur1 = head
        ret = {}
        while cur1:
            if cur1.val not in ret.keys():
                ret[cur1.val] = 1
            else:
                ret[cur1.val] += 1
            cur1 = cur1.next
        ret = [i for i,j in ret.items() if j==1]
        return ret
        a = ListNode(-1)
        while ret:
            a.next = ListNode(ret.pop(0))
            a = a.next
        return a.next
