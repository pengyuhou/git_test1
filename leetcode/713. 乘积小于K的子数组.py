class Solution:
    cnt = 0

    def numSubarrayProductLessThanK(self, nums: list, k: int) -> int:
        def fun(p):
            from functools import reduce
            return reduce(lambda x, y: x * y, p)

        l = 0
        r = 0
        ret = []

        def func(left, right):
            while left <= right and right < len(nums):
                if fun(nums[left:right + 1]) < k:
                    ret.append(nums[left:right + 1])
                    right += 1
                    self.cnt += 1
                else:
                    left += 1
                    right -= 1
            if right == len(nums):
                return left
            return right

        # res = func(l, r)
        # print(res)
        # ret = func(res[0] + 1, res[0] + 1)
        # print(ret)
        while True:
            l = func(l, l)
            l += 1
            if l==len(nums):
                break
        return self.cnt


print(Solution().numSubarrayProductLessThanK(nums=
                                             [10, 5, 2, 61, 2, 5, 8, 12], k=100))
