class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret = []


        while num:
            res = num % 2
            ret.insert(0, res)
            num = num // 2

        sum_ret = 0
        l = len(ret)

        for i in range(l - 1, -1, -1):
            if ret[i] == 1:
                ret[i] = 0
            else:
                ret[i] = 1
            sum_ret += ret[i] * pow(2,l-i-1)

        return sum_ret

if __name__ == '__main__':

    num = 2
    S=Solution()
    print(S.findComplement(num))









