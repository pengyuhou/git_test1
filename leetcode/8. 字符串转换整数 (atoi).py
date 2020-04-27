import re
class Solution:
    def myAtoi(self, s):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s=s.lstrip()
        rex=re.compile('^[\-\+]?\d+')
        num=rex.findall(s)
        num = int(*num)
        return max(min(num,INT_MAX),INT_MIN)


if __name__ == "__main__":
    s = "   -4193 with words     a"
    # s='42'
    # s="   -42"
    # s="words and 987"
    print(Solution().myAtoi(s))




