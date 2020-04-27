class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        res = [x for x in a if x != '']
        res.reverse()
        return ' '.join(res)


if __name__ == "__main__":
    s =  "  hello world!  "
    s="the sky is blue"
    s="a good   example"
    print(Solution().reverseWords(s))






