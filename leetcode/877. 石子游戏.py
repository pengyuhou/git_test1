class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        y = []
        l = []
        for i in range(len(piles)):
            if not i%2:
                y.append(max(piles[0],piles[-1]))
                if piles[0]>piles[-1]:
                    piles.pop(0)
                else:
                    piles.pop()
            else:
                y.append(max(piles[0], piles[-1]))
                if piles[0] > piles[-1]:
                    piles.pop(0)
                else:
                    piles.pop()
        return sum(y)>sum(l)



if __name__ == "__main__":

    print(Solution().stoneGame([5,3,4,5]))


