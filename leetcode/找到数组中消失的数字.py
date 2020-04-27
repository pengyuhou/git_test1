class Solution(object):
    def findDisappearedNumbers(self, nums):
        if nums==[]:
            return []
        size = len(nums)
        a = set(nums)
        a = list(a)
        a.sort()
        ret = []
        index = max(a)
        while index >= 1:
            if index not in a:
                ret.append(index)
            index -= 1
        for i in range(max(a) + 1, size + 1):
            ret.append(i)
        ret.sort()
        return ret

if __name__ == "__main__":
    # nums=[4,3,2,7,7,2,3,1]
    nums = [1,1]
    num1=[]
    s=Solution()
    print(s.findDisappearedNumbers(nums))



















