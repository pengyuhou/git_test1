class sports(object):
    def sport(self,nums):
        a = nums
        res = sorted(a,key=lambda x:x[0])
        stack = []
        count = 0
        for i in range(len(res)):
            count = max(count,len(stack))
            if not i:
                stack.append(res[i])
                continue
            if res[i][0]<=stack[-1][1]:
                stack.append(res[i])
            else:
                stack.pop()
                stack.append(res[i])
        return count

if __name__ == "__main__":
    a = [[0,30],[2,10],[12,17],[5,15],[13,18]]
    print(sports().sport(a))

