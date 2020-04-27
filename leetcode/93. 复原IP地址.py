"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

"""
class Solution(object):
    def restoreIpAddresses(self, s):
        ret = []
        def dfs(p,index,level,res):
            if level==5 or index>=len(s):
                if level==5 and index==len(s):
                    ret.append('.'.join(res))
                return
            for i in range(1,4):
                x=s[index:index+i]
                if int(x)<256 and  not str(x).startswith('0') or x=='0':
                    res.append(x)
                    dfs(p,index+i,level+1,res)
                    res.pop()
        res = []
        dfs(s,0,1,res)
        return ret


if __name__ == "__main__":
    print(Solution().restoreIpAddresses("010010"))
    print(int('017')<256)











