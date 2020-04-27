class Solution(object):
    def replaceSpaces(self, S, length):
        return S[:length].replace(' ','%20')


if __name__ == '__main__':
    s="               "
    l=5
    print(Solution().replaceSpaces(s,l))










