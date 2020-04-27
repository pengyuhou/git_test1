class Solution:
    def addToArrayForm(self, A, K) :
        return [int(i) for i in list(str(int(''.join([str(i) for i in A])) + K))]

if __name__ == "__main__":
    A = [2, 7, 4]
    K = 181
    print(Solution().addToArrayForm(A,K))







