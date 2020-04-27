class Solution(object):
    def topKFrequent(self, nums, k):
        a = {}
        for num in nums:
            if num not in a.keys():
                a[num] = 1
            else:
                a[num] += 1
        res = list(a.items())
        res=sorted(res,key=lambda x:x[1])
        q=[i for i,j in res[-k:]]
        q.reverse()
        return q



if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums,k))
