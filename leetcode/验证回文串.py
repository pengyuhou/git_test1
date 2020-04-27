class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        ret = []
        for i in s:
            if i.isalpha() or i.isdigit():
                ret.append(i)

        l = len(ret)
        for i in range(l):
            if ret[i].isalpha() and ret[i].isupper():
                ret[i] = ret[i].lower()

        for i in range(l // 2):
            if ret[i] != ret[l - 1 - i]:
                return False
        return True


if __name__ == '__main__':
    s="race a car"
    print(Solution().isPalindrome(s))





















