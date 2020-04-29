# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        cur1 = head
        ret = []
        while cur1:
            ret.append(cur1.val)
            cur1 = cur1.next

        def merge_sort(p):
            l = len(p)
            if l==1:
                return p
            ret = []
            mid = l//2
            left = merge_sort(p[:mid])
            right = merge_sort(p[mid:])
            index1 = 0
            index2 = 0

            while index1<len(left) and index2<len(right):
                if left[index1]<right[index2]:
                    ret.append(left[index1])
                    index1 += 1
                else:
                    ret.append(right[index2])
                    index2 += 1
            ret += left[index1:]
            ret += right[index2:]
            return ret

        if ret:
            res = merge_sort(ret)
        else:
            return head
        a = ListNode(-1)
        tmp = a
        while ret:
            a.next = ListNode(res.pop(0))
            a = a.next
        return tmp.next











