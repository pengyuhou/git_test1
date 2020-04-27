class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        arr=A
        return  sorted([i*i for i in arr])

if __name__ == '__main__':
    arr=[-4,-1,0,3,10]


    s=Solution()
    print(s.sortedSquares())



