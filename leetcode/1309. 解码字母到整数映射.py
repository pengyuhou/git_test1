class Solution:
    def freqAlphabets(self, s: str) -> str:
        a = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10#':'j','11#':'k','12#':'l','13#':'m','14#':'n','15#':'o','16#':'p','17#':'q','18#':'r','19#':'s','20#':'t','21#':'u','22#':'v','23#':'w','24#':'x','25#':'y','26#':'z'}
        l = len(s)
        ans = ''
        i = 0
        while i<l:
            if i+2<l:
                if s[i+2]=='#':
                    ans += a.get(s[i:i+3])
                    i += 3
                else:
                    ans += a.get(s[i])
                    i += 1
            else:
                ans += a.get(s[i])
                i += 1
        return ans





if __name__ == "__main__":
    s = "10#11#12"
    s = "1326#"
    s = "25#"
    s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    print(Solution().freqAlphabets(s))
