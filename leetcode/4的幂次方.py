class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<=0:
            return False
        while num>1:
            res=num%4
            if res!=0:
                return False
            num=num//4
        return True

if __name__ == "__main__":

    num=4
    print(Solution().isPowerOfFour(num))
















