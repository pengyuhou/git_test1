import re
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        s = s.strip()
        r = re.compile('^[\-\+]?\d+')
        res = r.findall(s)
        if res == []:
            return 0
        else:
            if int(res[0])>INT_MAX:
                return INT_MAX
            elif  int(res[0])<INT_MIN:
                return INT_MIN
            else:
                return int(res[0])

if __name__ == "__main__":
    print(Solution().myAtoi("4193 with words"))
