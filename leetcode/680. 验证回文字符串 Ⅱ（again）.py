class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ret = []
        left1 = 0
        right1 = len(s) - 1

        def fun(a, l, r):
            left = l
            right = r
            while right > left and a[left] == a[right]:
                left += 1
                right -= 1
            if right <= left:
                return True
            else:
                ret.append(left)
                ret.append(right)
                return False

        if fun(s, left1, right1):
            return True
        else:
            if fun(s, ret[0], ret[1] - 1):
                return True
            else:
                if fun(s, ret[0] + 1, ret[1]):
                    return True
                else:
                    return False


if __name__ == "__main__":
    print(Solution().validPalindrome('abvvRba'))
