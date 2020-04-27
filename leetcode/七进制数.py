class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return '0'
        ret = []
        if num >= 0:
            while num:
                res = num % 7
                num = num // 7
                ret.append(str(res))
            ret.reverse()
            return ''.join(ret)
        else:
            num = -num
            while num:
                res = num % 7
                num = num // 7
                ret.append(str(res))
            ret.reverse()
            return '-'+''.join(ret)

if __name__ == '__main__':
    num=5
    s=Solution()
    print(s.convertToBase7(num))





