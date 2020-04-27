class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        def dfs(sx,index,level,res):
            if level==5 or index>=len(sx):
                if len(res)==4 and index>=len(sx) and '.'.join(res.copy()) not in ret:
                    ret.append('.'.join(res.copy()))
                return
            for i in range(1,4):
                item = sx[index:index+i]
                if (0<=int(item)<=255 and not item.startswith('0')) or item == '0':
                    res.append(item)
                    dfs(sx,index+i,level+1,res)
                    res.pop()
        dfs(s,0,1,[])
        return ret


if __name__ == "__main__":
    # print(int('00'))
    print(Solution().restoreIpAddresses("00"))
