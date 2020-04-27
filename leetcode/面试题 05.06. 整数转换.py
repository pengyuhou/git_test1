
class Solution:
    def convertInteger(self, A: int, B: int) -> int:

        A &= 0xFFFFFFFF
        B &= 0xFFFFFFFF

        res = A ^ B
        count = 0
        while res:
            res &= res - 1
            count += 1
        return count



if __name__ == '__main__':
    print(Solution().convertInteger(17,9))
    
