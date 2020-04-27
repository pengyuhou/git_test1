import re
class Solution:
    def strToInt(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        s=s.strip()
        rex=re.compile('^[\+\-]?\d+')
        res=rex.findall(s)
        return min(max(int(*res),INT_MIN),INT_MAX)





if __name__ == "__main__":
    s="words and "
    # s = "          4193 with words"
    print(Solution().strToInt(s))
    # a={'123':123,'ads':'ll'}



