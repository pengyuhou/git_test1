class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index = 0
        flag = True
        ret = []
        for i in range(len(s)):
            ret.append([index,s[i]])
            if flag:
                index += 1
                if index == numRows:
                    index -= 2
                    flag = False
                    continue
            if not flag:
                index -= 1
                if index==-1:
                    index += 2
                    flag = True
                    continue
        a = {}
        for i in ret:
            if i[0] not in a.keys():
                a[i[0]] =  [i[1]]
            else:
                a[i[0]].append(i[1])
        ans = ''
        for i in a.values():
            ans += ''.join(i)
        return ans




if __name__ == "__main__":
    s = "LEETCODEISHIRING"
    numRows = 4
    print(Solution().convert(s, numRows))














