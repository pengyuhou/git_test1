class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=[]


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.l.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.l.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.l[0]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.l)==0:
            return True
        else:
            return False


if __name__ == '__main__':
    q=MyQueue()
    print(q.empty())
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    q.push(6)
    print(q.l)
    print(q.peek())
    print(q.pop())
    print(q.l)
    print(q.empty())


