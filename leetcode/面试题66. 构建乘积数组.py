class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        if a==[]:
            return []
        if a.count(0)>=2:
            return [0 for _ in range(len(a))]
        fi = 1
        for i in a:
            if i!=0:
                fi *= i
        ret = []
        if a.count(0)==1:
            cur = list(a).index(0)
            for i in  range(len(a)):
                if i==cur:
                    ret.append(fi)
                else:
                    ret.append(0)

            return ret
        for i in range(len(a)):

            ret.append(fi//a[i])
        return ret



if __name__ == "__main__":
    nums =[1,2,3,0,0]
    print(Solution().constructArr(nums))