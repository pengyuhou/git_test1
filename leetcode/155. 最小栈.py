class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.li = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.li or x <= self.li[-1]:
            self.li.append(x)

    def pop(self) -> None:
        a=self.stack.pop()
        if a==self.li[-1]:
            self.li.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.li[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
