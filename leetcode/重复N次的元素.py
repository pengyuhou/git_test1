class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a=A
        b = {}
        for i in range(len(a)):
            if a[i] not in b.keys():
                b[a[i]] = 1
            else:
                return a[i]

if __name__ == "__main__":
    a = [2,1,2,5,3,2]
    print(Solution().repeatedNTimes(a))




