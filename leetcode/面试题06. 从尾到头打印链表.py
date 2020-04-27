# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        cur = head
        ret=[]
        while cur:
            ret.append(cur.val)
            cur = cur.next

        ret.reverse()
        return ret

if __name__ == '__main__':
    a=[1, 2]
    a.reverse()
    print(a)





















