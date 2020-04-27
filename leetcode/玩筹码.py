class Solution:
    def minCostToMoveChips(self, chips):
        odd = 0
        dou = 0
        for i in chips:
            if i % 2:
                odd += 1
            else:
                dou += 1
        return odd if odd<dou else dou

if __name__ == "__main__":
    chips = [1,2,3]
    print(Solution().minCostToMoveChips(chips))









