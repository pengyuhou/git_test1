class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while True:
            r = 0
            while num != 0:
                res = num % 10
                num = num // 10

                r += res
            num = r
            if len(str(num)) == 1:
                break
        return num

if __name__ == '__main__':
    num=38
    while True:
        r=0
        while num != 0:
            res=num%10
            num =num //10

            r += res
        num=r
        if len(str(num))==1:
            break
    print(num)


