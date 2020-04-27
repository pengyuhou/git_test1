class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        ans = []
        x = r0
        y = c0
        dx = 0
        dy = 1
        flags = 1
        while len(ans) < R*C:
            for i in range(2):
                for _ in range(flags):
                    if 0 <= x < R and 0 <= y < C:
                        ans.append([x, y])
                    x += dx
                    y += dy
                dx,dy=dy,-dx
            flags += 1
        return ans


if __name__ == "__main__":
    R = 5
    C = 6
    r0 = 1
    c0 = 4
    print(Solution().spiralMatrixIII(R,C,r0,c0))