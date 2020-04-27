class Solution(object):
    def largestTriangleArea(self, points):
        ret=[]
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    a = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
                    b = ((points[i][0] - points[k][0]) ** 2 + (points[i][1] - points[k][1]) ** 2) ** 0.5
                    c = ((points[j][0] - points[k][0]) ** 2 + (points[j][1] - points[k][1]) ** 2) ** 0.5
                    p = (a + b + c) / 2
                    sx = p*(p-a)*(p-b)*(p-c)
                    ret.append(sx)
        return float(max(ret))**0.5




if __name__ == "__main__":
    points = [[35,-23],[-12,-48],[-34,-40],[21,-25],[-35,-44],[24,1],[16,-9],[41,4],[-36,-49],[42,-49],[-37,-20],[-35,11],[-2,-36],[18,21],[18,8],[-24,14],[-23,-11],[-8,44],[-19,-3],[0,-10],[-21,-4],[23,18],[20,11],[-42,24],[6,-19]]
    print(Solution().largestTriangleArea(points))














