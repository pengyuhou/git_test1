class Solution(object):
    def smallestRangeI(self, A, K):
        a=A
        k=K
        a_max = max(a)
        a_min = min(a)
        if a_max - k <= a_min+k:
            return 0
        else:
            return a_max-a_min-2*k


if __name__ == "__main__":
    A = [1]
    K = 0
    print(Solution().smallestRangeI(A,K))



