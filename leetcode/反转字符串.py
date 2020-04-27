class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        l1 = len(s) // 2

        for i in range(l1):
            s[i], s[l - 1 - i] = s[l - 1 - i], s[i]

if __name__ == '__main__':
    s = ["H","a","n","n","a","h"]



