class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        tmp = image[sr][sc]
        image[sr][sc]=newColor
        res = [[sr,sc]]
        while True:
            ret = []
            for x,y in res:
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xi = x + dx
                    yi = y + dy
                    if -1 < xi < m and -1 < yi < n:
                        if image[xi][yi]==tmp:
                            if tmp == newColor:
                                continue
                            image[xi][yi] = newColor
                            ret.append([xi,yi])
            res += ret
            if not ret:
                return image

if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2

    image = [[0,0,0],[0,1,1]]
    sr=1
    sc=1
    newColor=1
    print(Solution().floodFill(image,sr,sc,newColor))