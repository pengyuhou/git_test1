class Solution(object):
    def subarraysDivByK(self, a, k):
        from collections import defaultdict
        hash_map = defaultdict(int)
        hash_map[0] = 1
        val = 0
        ret = 0
        for i in range(len(a)):
            val += a[i]
            ret += hash_map[val % k]
            hash_map[val % k] += 1
        return ret


"""
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        from collections import defaultdict
        a = defaultdict(int)
        a[0] = 1
        ret = 0
        for i in range(len(nums)):
            count += nums[i]
            if count - k in  a.keys():
                ret += a[count-k]
            a[count] += 1
        return ret

"""

if __name__ == "__main__":
    print(Solution().subarraysDivByK([-1, 2, 9],
                                     2))
