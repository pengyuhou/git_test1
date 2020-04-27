class Solution:
    def generate(self, numRows):
        n=numRows
        if n==1:
            return [[1]]
        if n==2:
            return [[1],[1,1]]
        ret=[[1],[1,1]]
        if n>2:
            for i in range(3,n+1):
                a = [0 for i in range(i)]
                a[0],a[-1]=1,1
                for j in range(1,i-1):
                    a[j]=ret[i-2][j]+ret[i-2][j-1]
                ret.append(a)
            return ret

if __name__ == "__main__":
    n=5
    print(Solution().generate(n))





