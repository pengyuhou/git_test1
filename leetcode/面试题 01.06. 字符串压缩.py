class Solution:
    def compressString(self, S: str) -> str:
        s = S
        index = 0
        l = len(s)
        ret = []
        while index <= l - 1:
            count = 1
            if index+1<=l-1:
                while s[index] == s[index + 1]:
                    count += 1
                    index += 1
                    if index + 1 > l - 1:
                        break
            ret.append(s[index])
            ret.append(str(count))
            index += 1
        if len(''.join(ret))>=len(s):
            return s
        else:
            return ''.join(ret)



if __name__ == '__main__':
    s="abbccd"
    print(Solution().compressString(s))








