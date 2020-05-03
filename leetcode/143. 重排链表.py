# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return head
        cur1 = head
        ret = []
        while cur1:
            ret.append(cur1.val)
            cur1 = cur1.next
        left = 1
        right = len(ret) - 1
        res = [ret[0]]
        while left <= right:
            if left==right:
                res.append(ret[right])
                break
            res.append(ret[right])
            res.append(ret[left])
            right -= 1
            left += 1
        res = res[1:]
        while res:
            head.next = ListNode(res.pop(0))
            head = head.next
