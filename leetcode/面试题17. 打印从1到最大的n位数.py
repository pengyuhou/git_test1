class Solution:
    def printNumbers(self, n):
        return list(range(1,int('9' * n)+1))

if __name__ == "__main__":
    n=1
    print(Solution().printNumbers(3))

