# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tmp1 = head
        ret = []
        while tmp1:
            ret.append(tmp1.val)
            tmp1 = tmp1.next
        for i in range(len(ret)):
            if not i%2 and i+1<len(ret):
                ret[i],ret[i+1]=ret[i+1],ret[i]
        a = ListNode(-1)
        while ret:
            a.next = ListNode(ret.pop(0))
            a = a.next
        return a.next




if __name__ == "__main__":
    print(Solution().swapPairs())













