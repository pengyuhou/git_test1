class Solution(object):
    def hIndex(self, citations):
        if citations==[]:
            return 0
        res = sorted(citations, reverse=True)
        ret = []
        for i in range(len(res)):
            if i+1>=res[i]:
                ret.append(res[i])
            else:
                ret.append(i+1)
        return max(ret)

if __name__ == "__main__":
    nums = [3,0,6,1,5,6,7,4,3,5,6,7,999,888,777,666,555,666,444,776543]
    print(Solution().hIndex(nums))
    