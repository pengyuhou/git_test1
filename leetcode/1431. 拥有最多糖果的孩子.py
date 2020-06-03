class Solution:
    def kidsWithCandies(self, candies, extraCandies: int) -> list:
        max_val = max(candies)
        ret = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_val:
                ret.append(True)
            else:
                ret.append(False)
        return ret


print(Solution().kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
