a=10


class Solution(object):

    def isPalindrome(self, x):
        x=str(x)
        for i in range(len(x)):
            j=len(x)-i-1
            if x[i] != x[j]:
                return False
        return True


print(Solution().isPalindrome(a))






