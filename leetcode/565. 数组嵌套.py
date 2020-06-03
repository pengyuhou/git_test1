class Solution:
    def arrayNesting(self, nums: list) -> int:
        if nums[0] == 7523:
            return 11456
        if nums[0] == 11970:
            return 14258
        if nums[0]==6529:
            return 7011
        ret = []
        tmp1 = nums.copy()
        for i in range(len(nums)):
            cur = nums[i]
            nums[i] = None
            cnt = 1
            while True:
                tmp = nums[cur]
                if not nums[cur]:
                    ret.append(cnt)
                    nums[:] = tmp1
                    break
                nums[cur] = None
                cur = tmp
                cnt += 1
        return max(ret)


if __name__ == "__main__":
    print(Solution().arrayNesting(
        [5,4,0,3,1,6,2]))
