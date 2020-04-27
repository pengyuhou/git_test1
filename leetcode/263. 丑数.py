class Solution:
    def isUgly(self, num: int) -> bool:
        if num==0:
            return False
        while not num%2:
            num //= 2
        while not num%3:
            num //= 3
        while not num%5:
            num //= 5
        return 1==num












