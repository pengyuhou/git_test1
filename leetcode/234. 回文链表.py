# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        ret = []
        while cur:
            ret.append(cur.val)
            cur = cur.next
        l = len(ret)
        for i in range(l//2):
            if ret[i]!=ret[l-1-i]:
                return False
        return True








