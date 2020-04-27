class MinStack:

    def __init__(self):
        self._=[]
        self.res=[]
    def push(self, x: int) -> None:
        if not self.res:
            self.res.append(x)
        else:
            if x<=self.res[-1]:
                self.res.append(x)
        self._.append(x)

    def pop(self) -> None:
        if self.top()==self.res[-1]:
            self.res.remove(self.res[-1])
            self._.pop()
        else:
            self._.pop()

    def top(self) -> int:
        return self._[-1]
    def min(self) -> int:
        return self.res[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()