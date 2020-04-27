class Solution(object):
    def twoSum(self, numbers, target):
        a=sorted(list(set(numbers)))
        ret=[]
        for i in range(len(a)):
            if i == 0:
                num=numbers.count(a[i])
                ret.append([a[i], num])
            else:
                num = numbers.count(a[i])
                num += ret[i-1][1]
                ret.append([a[i],num])
        for i in range(len(ret)-1):
            for j in range(i,len(ret)):
                if ret[i][0]+ret[j][0] == target:
                    if ret[i][0] != ret[j][0]:
                        return [ret[i][1],ret[j][1]]
                    else:
                        return [ret[i][1]-1,ret[j][1]]



if __name__ =="__main__":
    numbers = [0,0,3,4]
    target = 0
    print(Solution().twoSum(numbers,target))






