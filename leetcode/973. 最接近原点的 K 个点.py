class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        res = sorted(points, key=lambda x: (x[0] ** 2 + x[1] ** 2) ** 0.5)
        return res[:K]


class Solution1(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        res = map(lambda x: (x[0] ** 2 + x[1] ** 2) ** 0.5, points)
        r = list(res)
        a = {i: j for i, j in zip(range(len(r)), r)}
        ret = sorted(list(a.items()), key=lambda x: x[1])
        ans = []
        for i in range(K):
            ans.append(points[ret[i][0]])
        return ans




if __name__ == "__main__":
    points = [[1, 3], [-2, 2]]
    K = 1
    print(Solution1().kClosest(points, K))
