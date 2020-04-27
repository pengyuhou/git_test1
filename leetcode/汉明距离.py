class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        l_x = []
        while x:
            res = x % 2
            x = x // 2
            l_x.append(res)

        l_y = []
        while y:
            res = y % 2
            y = y // 2
            l_y.append(res)

        len_x = len(l_x)
        len_y = len(l_y)
        if len_x > len_y:
            while len(l_x) > len(l_y):
                l_y.append(0)

        if len_x < len_y:
            while len(l_x) < len(l_y):
                l_x.append(0)
        sum = 0
        for i, j in zip(l_x, l_y):
            if i != j:
                sum += 1
        return sum

if __name__ == '__main__':
    x = 10
    y = 67
    s=Solution()
    print(s.hammingDistance(x,y))









