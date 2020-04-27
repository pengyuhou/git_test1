class Solution(object):
    def isMonotonic(self, A):
        a=A
        if a[0]<a[-1]:
            x=sorted(a)
            return x==a
        else:
            x=sorted(a,reverse=True)
            return x==a

if __name__ == "__main__":
    a = [1,2,2,3]
    a=[6,5,4,9]
    a=[11,13,11]
    print(Solution().isMonotonic(a))

