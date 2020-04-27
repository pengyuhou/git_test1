num1 = "2"
num2 = "3"

class Solution(object):
    def multiply(self, num1, num2):
        ret=int(num1)*int(num2)
        return str(ret)
s=Solution()
print(type(s.multiply(num1, num2)))


