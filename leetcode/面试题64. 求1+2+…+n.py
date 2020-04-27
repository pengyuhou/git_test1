class Solution:
    def sumNums(self, n: int) -> int:
        return int(((n+1)*n)/2)



if __name__ == "__main__":
    n=9
    print(Solution().sumNums(n))