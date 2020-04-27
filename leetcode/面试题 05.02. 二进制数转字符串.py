class Solution:
    def printBin(self, num: float) -> str:
        ret = []

        if num <= 0 or num >= 1:
            return "ERROR"
        while num:
            num = num * 2
            ret.append(str(num)[0])
            if num >= 1:
                num -= 1
            if len(ret) > 30:
                return "ERROR"
        return '0.' + ''.join(ret)


if __name__ == "__main__":
    print(Solution().printBin(0))



