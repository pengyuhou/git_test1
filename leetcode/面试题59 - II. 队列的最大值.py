class MaxQueue:

    def __init__(self):
        self.li = []
        self.fuzhu = []

    def max_value(self) -> int:
        if self.fuzhu!=[]:
            return self.fuzhu[0]
        else:
            return -1



    def push_back(self, value: int) -> None:
        self.li.insert(0,value)
        while self.fuzhu and self.fuzhu[-1]<value:
            self.fuzhu.pop()
        self.fuzhu.append(value)


    def pop_front(self) -> int:
        if self.li!=[]:
            a = self.li.pop()
            if a==self.fuzhu[0]:
                self.fuzhu.pop(0)
            return a

        else:
            return -1


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

if __name__ == "__main__":
    a=MaxQueue()



