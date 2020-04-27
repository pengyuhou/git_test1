class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        queue = [[0,0]]
        count = 1
        mask = [[0 for _ in range(n)] for _ in range(m)]
        mask[0][0]=1
        while queue:
            l = len(queue)
            for _ in range(l):
                x,y=queue.pop(0)
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    xi = x + dx
                    yi = y + dy
                    if 0<=xi<m and 0<=yi<n and mask[xi][yi]==0:
                        v = sum([int(i) for i in str(xi)])+sum([int(i) for i in str(yi)])
                        if v<=k:
                            mask[xi][yi]=1
                            queue.append([xi,yi])
                            count += 1
        return count



if __name__ == '__main__':
    m = 3
    n = 2
    k = 17
    print(Solution().movingCount(m,n,k))












