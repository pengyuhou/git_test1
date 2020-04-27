class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        l = len(stones)
        while l != 1:
            res = stones[-1] - stones[-2]
            stones = stones[:-2]
            stones.append(res)
            stones.sort()
            l = len(stones)
        return stones[0]


if __name__ == "__main__":
    stones=[3,4,7,8,5]

    print(Solution().lastStoneWeight(stones))





