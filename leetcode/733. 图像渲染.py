"""
输入: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],[2,2,0],[2,0,1]]
"""
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        m = len(image)  # 行数
        n = len(image[0])  # 列数
        image_cp = image.copy()
        cl_pre = image_cp[sr][sc]
        image_cp[sr][sc] = newColor
        res = [[sr,sc]]
        while True:
            l =len(res)
            for x,y in res:
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xi = x + dx
                    yi = y + dy
                    if 0 <= xi < m and 0 <= yi < n:
                        if image_cp[xi][yi] == cl_pre:
                            if cl_pre == newColor:
                                continue
                            image_cp[xi][yi] = newColor
                            res.append([xi,yi])
            if len(res)==l:
                break
        return image_cp

if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2

    image=[[0, 0, 0], [0, 1, 1]]
    sr=1
    sc=1
    newColor=1

    print(Solution().floodFill(image,sr,sc,newColor))




