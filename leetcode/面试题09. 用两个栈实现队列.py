class CQueue:

    def __init__(self):
        self.li=[]



    def appendTail(self, value: int) -> None:
        self.li.append(value)


    def deleteHead(self) -> int:
        if self.li==[]:
            return -1
        return self.li.pop(0)



# Your CQueue object will be instantiated and called as such:



if __name__ == "__main__":
    obj = CQueue()
    obj.appendTail(2)
    obj.appendTail(3)
    print(obj.li)
    print(obj.deleteHead())
    print(obj.deleteHead())
    print(obj.deleteHead())
