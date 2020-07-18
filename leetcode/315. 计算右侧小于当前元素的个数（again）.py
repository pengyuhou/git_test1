class Solution(object):
    def countSmaller(self, nums):
        if not nums:
            return []
        import bisect
        a = nums[::-1]
        ret = [0]
        res = [a[0]]
        for i in range(1, len(a)):
            bisect.insort_left(res, a[i])
            ret.append((bisect.bisect_left(res, a[i])))
        return ret[::-1]

if __name__ == "__main__":
    print(Solution().countSmaller([5, 2, 6, 1]))
