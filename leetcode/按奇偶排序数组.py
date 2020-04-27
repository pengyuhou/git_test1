class Solution(object):
    def sortArrayByParity(self, A):
        ji = []
        ou = []
        nums=A
        for i in nums:
            if i % 2:
                ji.append(i)
            else:
                ou.append(i)
        ret = []
        for i in range(len(ou)):
            ret.append(ou.pop())
        ret += ji
        return ret

if __name__ == "__main__":
    nums = [3,1,2,4]

    print(ret)



