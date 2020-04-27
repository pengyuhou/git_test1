class Solution(object):
    def reverseLeftWords(self, s, n):
        return s[n:]+s[:n]

if __name__ == "__main__":
    s = "lrloseumgh"
    k = 6
    print(Solution().reverseLeftWords(s,k))

