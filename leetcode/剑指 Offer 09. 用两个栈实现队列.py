class CQueue:

    def __init__(self):
        self.a = []


    def appendTail(self, value: int) -> None:
        self.a.append(value)


    def deleteHead(self) -> int:
        try:
            return self.a.pop(0)
        except:
            return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()




































