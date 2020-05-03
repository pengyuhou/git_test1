# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur1 = head
        ret = []
        while cur1:
            ret.append(cur1.val)
            cur1 = cur1.next
        for i in range(1, len(ret)):
            key = ret[i]
            j = i - 1
            while j >= 0 and key < ret[j]:
                ret[j + 1], ret[j] = ret[j], key
                j -= 1
        a = ListNode(-1)
        tmp = a
        while a:
            a.next = ListNode(ret.pop(0))
            a = a.next
        return tmp.next



a = [4,3,1]
print(len(a))
print(a)
index = 0
l = len(a)
for i in range(1, l):
    key = a[i]
    j = i - 1
    while j >= 0 and key < a[j]:
        a[j + 1],a[j] = a[j],key
        j -= 1

print(len(a))
print(a)
