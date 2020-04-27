# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# head = [4,5,1,9], val = 5

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        cur = head
        if cur.val==val:
            head=cur.next
        else:
            while cur.next.val!=val:
                cur = cur.next
            cur.next=cur.next.next
        return head

if __name__ == "__main__":
    a=[1,2]
    a=[3]+a
    print(a)










