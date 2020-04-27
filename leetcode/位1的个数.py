class Solution:
    def hammingWeight(self, n: int) -> int:
        a=n
        count = 0
        while a:
            res = a % 2
            a = a // 2
            if res == 1:
                count += 1

        return count

if __name__ == '__main__':
    a = 0b11111111111111111111111111111101
    S=Solution()
    print(S.hammingWeight(a))




