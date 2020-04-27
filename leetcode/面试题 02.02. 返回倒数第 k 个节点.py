# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 输入： 1->2->3->4->5 和 k = 2
# 输出： 4
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        cur=head
        count = 0
        while cur:
            count += 1
            cur=cur.next
        cur = head
        num = count - k + 1
        while cur:
            num-= 1
            if not num :
                break
            cur=cur.next
        return cur.val





