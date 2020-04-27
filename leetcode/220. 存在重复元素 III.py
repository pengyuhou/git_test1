class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        res = list(enumerate(nums))
        ret = sorted(res, key=lambda x: x[1])
        for i in range(len(ret) - 1):
            for j in range(i + 1, len(ret)):
                if abs(ret[i][1] - ret[j][1]) <= t and abs(ret[i][0] - ret[j][0]) <= k:
                    return True
        return False


