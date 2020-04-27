# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head1 = head
        num = 0
        if head and not head.next:
            return None
        while head1:
            head1 = head1.next
            num += 1
        pre = ListNode(-1)
        tmp = pre
        cur = head
        pre.next = cur
        index = num - n
        while index > 0 and pre:
            pre = cur
            cur = cur.next
            index -= 1
        pre.next = cur.next
        return tmp.next
