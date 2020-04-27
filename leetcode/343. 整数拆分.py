class Solution:
    def integerBreak(self, n: int) -> int:
        ret=[None,1,2,4,6,9]
        if n<7:
            return ret[n-1]
        else:
            index = 7
            while index<=n:
                ret.append(3*ret[index-4])
                index += 1
            return ret[-1]






if __name__ == "__main__":

    print(Solution().integerBreak(10))