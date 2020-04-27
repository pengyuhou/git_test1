class Solution:
    def findMaxConsecutiveOnes(self, nums):
        nums = [str(i) for i in nums]
        x = "".join(nums)

        res = x.split('0')

        return len(max(res))

class Solution2(object):
    def findMaxConsecutiveOnes(self, nums):
        cur = 0
        l = len(nums)
        ret=0
        while cur < l:
            count=0
            while cur <l and nums[cur]:
                count += 1
                cur += 1
            if cur < l and not nums[cur]:
                if count>ret:
                    ret=count
            if cur == l :
                if count>ret:
                    ret=count
            cur += 1
        return ret


if __name__ == "__main__":
    nums = [1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,0]
    print(Solution2().findMaxConsecutiveOnes(nums))




