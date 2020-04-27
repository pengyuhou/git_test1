class Solution:
    def isUnique(self, astr: str) -> bool:
        for i in astr:
            if astr.count(i)>1:
                return False
        return True



if __name__ == "__main__":
    s = "abc"
    print(Solution().isUnique(s))






