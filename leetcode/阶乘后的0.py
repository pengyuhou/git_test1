class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = n - n % 5
        sum1 = 1
        while n > 0:
            sum1 *= n
            n -= 1
        index = len(str(sum1)) - 1

        count = 0

        for i in range(index, 0, -1):
            if str(sum1)[i] == '0':
                count += 1
            else:
                break
        return count

if __name__ == '__main__':
    n=1780
    s=Solution()
    print(s.trailingZeroes(n))







