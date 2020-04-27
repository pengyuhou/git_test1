class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A=='' and B=='':
            return True
        a=list(A)
        b=list(B)
        if len(a) != len(b):
            return False

        for i in range(len(A)):
            x=b.pop()
            b.insert(0,x)
            if b==a:
                return True
        return False



if __name__ == "__main__":
    A = ''
    B = 'ads'
    # b=(list(B))
    # c=b.pop()

    # print(b)
    print(Solution().rotateString(A,B))







