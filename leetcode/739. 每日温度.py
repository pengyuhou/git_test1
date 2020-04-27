class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(len(T)-1):
            key = T[i]
            index = i + 1
            flag =True
            while index < len(T):
                if T[index]>key:
                    ret.append(index-i)
                    flag =False
                    break
                index += 1
            if flag:
                ret.append(0)
        ret.append(0)
        return ret


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temperatures))
