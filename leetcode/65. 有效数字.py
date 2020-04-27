class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            a=float(s)
            return True
        except:
            return False








if __name__ == "__main__":


    print(Solution().isNumber('123'))
