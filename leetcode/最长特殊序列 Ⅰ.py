class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b:
            return -1
        else:
            return len(a) if len(a)>len(b) else len(b)


if __name__== "__main__":
    a="abad"
    b="cdc"
    print(Solution().findLUSlength(a,b))



