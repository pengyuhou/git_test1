class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mins=[]

        self.list_ = []


    def push(self, x: int) -> None:
        if not self.mins:
            self.mins.append(x)
        else:
            if x<self.mins[-1]:
                self.mins.append(x)

        self.list_.append(x)

    def pop(self) -> None:
        self.list_.pop()


    def top(self) -> int:
        return self.list_[-1]


    def getMin(self) -> int:
        return min(self.list_)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    a=MinStack()
    a.push(1)
    a.push(2)
    a.push(3)
    print(a.getMin())
    a.pop()
    print(a.top())


