class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')



if  __name__ == "__main__":
    a=0b11111111111111111111111111111101
    print(Solution().hammingWeight(a))




