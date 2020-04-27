# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = l1
        ret = []
        while cur:
            ret.append(cur.val)
            cur = cur.next
        cur = l2
        ret1 = []
        while cur:
            ret1.append(cur.val)
            cur = cur.next
        count1 = 0
        index = 0
        for i in range(len(ret)-1,-1,-1):
            count1 += ret[i]*(10**index)
            index += 1

        index = 0
        count2 = 0
        for i in range(len(ret1) - 1, -1, -1):
            count2 += ret1[i] * (10 ** index)
            index += 1
        return count1+count2








