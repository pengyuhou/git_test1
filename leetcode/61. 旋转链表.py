# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        a1 = head
        ret = []
        while a1:
            ret.append(a1.val)
            a1 = a1.next
        l = len(ret)
        if k > l:
            index = k%l

            res = ret[l-index:]+ret[:l-index]

        else:
            res = ret[l-k:]+ret[:l-k]
        x = ListNode(-1)
        tmp = x
        while res:
            x.next = ListNode(res.pop(0))
            x = x.next
        return tmp.next

if __name__ == "__main__":
    k = 2000000000
    ret = [1, 2, 3, 4, 5]
    print(2000000000%3)
