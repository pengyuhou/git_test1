class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ret=[]
        for i in range(len(A)):
            for j in range(len(B)):
                A[i], B[j] = B[j], A[i]
                if sum(A) == sum(B):

                    ret.append(B[j])
                    ret.append(A[i])
                    return ret
                A[i], B[j] = B[j], A[i]

if __name__ == '__main__':
    A = [1, 2, 5]
    B = [2, 4]
    s=Solution()
    print(s.fairCandySwap(A,B))









