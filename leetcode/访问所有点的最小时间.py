class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sum_distance = 0
        for i in range(len(points) - 1):
            s1 = abs(points[i][0] - points[i + 1][0])
            s2 = abs(points[i][1] - points[i + 1][1])

            sum_distance += s1 if s1 > s2 else s2
        return sum_distance



if __name__ == '__main__':
    points = [[3, 2], [-2, 2]]









