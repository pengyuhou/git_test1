class Solution(object):
    def merge(self, intervals):
        def fun1(i, nums):
            ret = []
            while i < len(nums):
                if i == len(nums) - 1:
                    ret.append(nums[i])
                    break
                if nums[i + 1][0] <= nums[i][1] <= nums[i + 1][1]:
                    ret.append([nums[i][0], nums[i + 1][1]])
                    i += 2
                    continue
                else:
                    ret.append(nums[i])
                i += 1
            return ret
        def fun2(mat):
            ans = []
            index = 0
            while index < len(mat):
                if index == len(mat) - 1:
                    ans.append(mat[index])
                    index += 1
                    break
                if mat[index][1] >= mat[index + 1][1]:
                    ans.append(mat[index])
                    index += 2
                    continue
                else:
                    ans.append(mat[index])
                index += 1
            return ans

        res = sorted(intervals, key=lambda x: x[0])
        intervals = res
        while True:
            l = len(intervals)
            intervals = fun2(intervals)
            if l==len(intervals):
                break
        ans = intervals[:]
        while True:
            l = len(ans)
            ans = fun1(0, ans)
            if l==len(ans):
                break
        return ans



if __name__ == "__main__":
    print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
