class Solution:
    def countDigitOne(self, n: int) -> int:
        ret = 1
        for i in range(2,n+1):
            x = str(i)
            ret += x.count('1')
        return ret
class Solution(object):
    def countDigitOne(self, n):
        string = str(n)
        length = len(string)
        if n == 0:
            return 0
        if 1 <= n <= 9:
            return 1
        if string[0] == "1":
            return n % (10**(length-1)) + (length-1) * 10 ** (length-2) + 1 + self.countDigitOne(n % (10**(length-1)))
        return 10**(length-1) + 10**(length-2)*int(string[0])*(length-1)+self.countDigitOne(n % (10**(length-1)))



if __name__ == "__main__":
    print(Solution().countDigitOne(500))

