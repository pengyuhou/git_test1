class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {}
        for i in s:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1
        ret = 0
        flag = False
        for i in a.values():
            if not i % 2:
                ret += i
            else:
                if not flag:
                    flag = True
                    ret += 1
                ret += i - 1
        return ret



if __name__ == "__main__":
    s = "abccccdd"
    print(Solution().longestPalindrome(s))





