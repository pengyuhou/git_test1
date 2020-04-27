class Solution:
    def fun(self, s):
        res = ''
        for i in range(len(s)):
            if not i:
                tmp = s[i]
                count = 1
                if i == len(s) - 1:
                    res += str(count)
                    res += str(tmp)
            else:
                if tmp == s[i]:

                    count += 1
                    if i == len(s) - 1:
                        res += str(count)
                        res += str(tmp)
                    continue
                else:
                    res += str(count)
                    res += str(tmp)

                    tmp = s[i]
                    count = 1
                    if i == len(s) - 1:
                        res += str(count)
                        res += str(tmp)
        return res

    def countAndSay(self, n: int) -> str:
        a = '1'
        for i in range(n-1):
            a = self.fun(a)
        return a


if __name__ == "__main__":
    print(Solution().countAndSay(30))
