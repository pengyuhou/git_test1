class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        return sorted([[i, j] for i in range(R) for j in range(C)], key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))



if __name__ == "__main__":
    R = 2
    C = 3
    r0 = 1
    c0 = 2
    print(Solution().allCellsDistOrder(R,C,r0,c0))





























