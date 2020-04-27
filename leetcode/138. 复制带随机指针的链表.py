"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        a = {None:None}
        tmp1 = head
        while tmp1:
            a[tmp1] = Node(tmp1.val)
            tmp1 = tmp1.next
        tmp2 = head
        while tmp2:
            a[tmp2].next = a[tmp2.next]
            a[tmp2].random = a[tmp2.random]
            tmp2 = tmp2.next
        return a[head]


















