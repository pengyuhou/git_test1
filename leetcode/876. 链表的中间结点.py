# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        index = head
        lim = count//2
        while lim:
            index = index.next
            lim -= 1
        return index



