class Solution(object):
    def sortArrayByParityII(self, A):
        num = A
        ji = []
        ou = []
        for i in num:
            if i % 2:
                ji.append(i)
            else:
                ou.append(i)
        ret = []
        for i in range(len(ji)):
            ret.append(ou[i])
            ret.append(ji[i])
        return ret

if __name__ == "__main__":
    num=[4, 2, 5, 7]
    print(Solution().sortArrayByParityII(num))

