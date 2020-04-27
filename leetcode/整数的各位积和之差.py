class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = list(str(n))
        len_n = len(n)
        sum_n = 0
        mul_n = 1
        for i in range(len_n):
            sum_n += int(n[i])
            mul_n *= int(n[i])
        return mul_n - sum_n

if __name__ == '__main__':
    n = 4421






