# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        ret = []
        for i in lists:
            while i:
                ret.append(i.val)
                i = i.next
        ret.sort()
        a = ListNode(-1)
        tmp = a
        while ret:
            a.next = ListNode(ret.pop(0))
            a = a.next
        return tmp.next
