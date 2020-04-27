class MyStack(object):
    def __init__(self):
        self.stack=[]

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.stack == []:
            return True
        else:
            return False


if __name__ == "__main__":
    s=MyStack()
    s.push(1)
    s.push(2)
    print(s.top())
    print(s.pop())
    print(s.empty())
    print(s.stack)
    print(s.pop())
    print(s.empty())
    print(s.stack)






