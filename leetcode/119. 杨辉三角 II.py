class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n = rowIndex
        if n==0:
            return [1]
        if n==1:
            return [1,1]
        if n==2:
            return [1,2,1]
        if n>=3:
            res =[1,2,1]
            while n>=len(res):
                ret =[None]*(len(res)+1)
                ret[0],ret[-1]=1,1
                for i in range(1,len(ret)-1):
                    ret[i] = res[i]+res[i-1]
                res = ret
            return ret



if __name__ == "__main__":
    n = 4
    print(Solution().getRow(n))








