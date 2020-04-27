class Solution(object):
    def maxCount(self, m, n, ops):
        if ops==[]:
            return m*n
        a = float('inf')
        b = float('inf')
        for i,j in ops:
            a = min(a,i)
            b = min(b,j)
        return a*b

if __name__ == "__main__":
    m = 18
    n = 3
    # operations= []
    operations = [[16,1],[14,3],[14,2],[4,1],[10,1],[11,1],[8,3],[16,2],[13,1],[8,3],[2,2],[9,1],[3,1],[2,2],[6,3]]
    # operations = [[2,1],[1,2]]
    # operations = [[1,4],[5,5],[4,9],[1,10],[6,2],[1,11],[4,6],[2,2],[3,15],[6,14],[1,17],[2,8],[4,7],[2,7]]
    print(Solution().maxCount(m,n,operations))