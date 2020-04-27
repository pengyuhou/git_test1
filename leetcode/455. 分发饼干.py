class Solution1:
    def findContentChildren(self, g, s):
        count = 0
        for i in range(len(g)):
            x = None
            for j in range(len(s)):
                if g[i] <= s[j]:
                    if not x:
                        x = s[j]
                    else:
                        if x > s[j]:
                            x = s[j]
            if x:
                count += 1
                s.remove(x)
        return count

class Solution:
    def findContentChildren(self, g, s):
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        index1 = len(g) - 1
        index2 = len(s) - 1
        count = 0
        while index1 >= 0 and index2 >= 0:
            if g[index1] <= s[index2]:
                count += 1
                index1 -= 1
                index2 -= 1
            else:
                index2 -= 1
        return count


if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1]
    print(Solution().findContentChildren(g,s))










    # print(Solution().findContentChildren(g,s))





