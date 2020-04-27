class Solution(object):
    def largestPerimeter(self, A):
        a=A
        a.sort()
        l = len(a)
        for i in range(l - 1, 1, -1):
            if a[i] + a[i - 2] > a[i - 1] and a[i] + a[i - 1] > a[i - 2] and a[i - 1] + a[i - 2] > a[i] and a[i - 2] - a[i - 1] < a[i] and a[i - 2] - a[i] < a[i - 1] and a[i - 1] - a[i] < a[i - 2]:
                return a[i]+a[i-1]+a[i-2]
        return 0

if __name__ == "__main__":
    a=[3, 2, 3]
    a=[1, 2, 1]
    a=[3,2,3,4]
    a=[2,1,2]
    print(Solution().largestPerimeter(a))











