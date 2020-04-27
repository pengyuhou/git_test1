class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        a = {}
        for i in range(len(nums)):
            if nums[i] not in a.keys():
                a[nums[i]] = [i]
            else:
                a[nums[i]].append(i)
        res = list(a.values())
        for i in range(len(res)):
            for j in range(len(res[i]) - 1):
                if abs(res[i][j] - res[i][j + 1])<=k:
                    return True
        return False



if __name__ == "__main__":
    nums = [1,2,3,1,2,3]
    k = 2
    print(Solution().containsNearbyDuplicate(nums, k))
