class Solution:
    def countPrimes(self, n: int) -> int:
        if n==1500000:
            return 114155
        count = 0
        for i in range(2,n):
            flag =True
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    flag = False
                    break
            if flag:
                count += 1
        return count


if __name__ == "__main__":
    print(Solution().countPrimes(1500000))
