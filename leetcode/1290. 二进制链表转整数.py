# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur=head
        index = 0
        while cur:
            index += 1
            cur = cur.next
        cur1 = head
        amount = 0
        while cur1:
            amount += cur1.val * 2 **(index -1)
            cur1 = cur1.next
            index -= 1
        return amount

if __name__ == "__main__":
    print(2**5)
