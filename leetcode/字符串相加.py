class Solution(object):
    def addStrings(self, num1, num2):

        i = len(num1) - 1
        j = len(num2) - 1
        res = 0
        ret = []
        while i >= 0 or j >= 0:
            if i > -1 and j > -1:
                c_x = int(num1[i])
                c_y = int(num2[j])
            if i == -1 and j > -1:
                c_x = 0
                c_y = int(num2[j])
                i = 0
            if j == -1 and i > -1:
                c_y = 0
                c_x = int(num1[i])
                j = 0
            c = c_x + c_y
            c = c + res
            ret_s = c % 10
            ret.append(ret_s)
            res = c // 10
            i -= 1
            j -= 1
            if i == -1 and j == -1:
                ret.append(res)
                ret.reverse()
                ret = [str(i) for i in ret]
                a = ''.join(ret)
                if a[0] == '0':
                    return  a[1:]
                else:
                    return a




# class Solution1:
#     def addStrings(self, num1: str, num2: str) -> str:
#         res = ""
#         i, j, carry = len(num1) - 1, len(num2) - 1, 0
#         while i >= 0 or j >= 0:
#             n1 = int(num1[i]) if i >= 0 else 0
#             n2 = int(num2[j]) if j >= 0 else 0
#             tmp = n1 + n2 + carry
#             carry = tmp // 10
#             res = str(tmp % 10) + res
#             i, j = i - 1, j - 1
#         return "1" + res if carry else res

# class Solution2(object):
#     def addStrings(self, num1, num2):
#





if __name__ == '__main__':
    # s=Solution()
    # print(s.addStrings('1','2'))
    str1='3'
    str2='19'
    s=Solution()
    print(s.addStrings(str1,str2))

    # i=len(str1)-1
    # j=len(str2)-1
    # res=0
    # ret=[]
    # while i>=0 or j >=0:
    #     if i >-1 and j>-1:
    #         c_x=int(str1[i])
    #         c_y=int(str2[j])
    #     if i==-1 and j>-1:
    #         c_x=0
    #         c_y=int(str2[j])
    #         i=0
    #     if j==-1 and i>-1:
    #         c_y=0
    #         c_x=int(str1[i])
    #         j=0
    #     c = c_x + c_y
    #     c = c + res
    #     ret_s=c%10
    #     ret.append(ret_s)
    #     res = c//10
    #     i -= 1
    #     j -= 1
    #     if i==-1 and j==-1:
    #         ret.append(res)
    #         ret.reverse()
    #         ret=[str(i) for i in ret]
    #         a=''.join(ret)
    #         if a[0] == '0':
    #             print(a[1:])
    #         else:
    #             print(a)
    #
    #         break


