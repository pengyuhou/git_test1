class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        from collections import defaultdict
        d = defaultdict(int)
        for i in matrix:
            if i[0]:
                d[tuple([1 - x for x in i])] += 1
            else:
                d[tuple(i)] += 1
        return max(d.values())


if __name__ == "__main__":
    print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 0]]))
