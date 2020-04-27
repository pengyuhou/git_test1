class Solution:
    def reverseWords(self, s: str) -> str:
        ret = []
        index = 0
        while index < len(s):
            tmp = []
            flag = False
            while index < len(s) and s[index] != ' ':
                tmp.append(s[index])
                index += 1
                flag = True
            if flag:
                ret.append(''.join(tmp))
            index += 1
        print(ret)
        ret.reverse()

        return ' '.join(ret)


if __name__ == "__main__":
    s = "  hello world!  "
    print(Solution().reverseWords(s))
