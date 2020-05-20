class Solution1(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(len(T) - 1):
            key = T[i]
            index = i + 1
            flag = True
            while index < len(T):
                if T[index] > key:
                    ret.append(index - i)
                    flag = False
                    break
                index += 1
            if flag:
                ret.append(0)
        ret.append(0)
        return ret


class Solution(object):
    def dailyTemperatures(self, t):
        t.reverse()
        t = list(enumerate(t))
        stack = [t[0]]
        ret = [0 for _ in range(len(t))]
        for i in range(1, len(t)):
            flag = True
            while t[i][1] >= stack[-1][1]:
                stack.pop()
                if not stack:
                    flag = False
                    stack.append(t[i])
                    ret[i] = 0
                    break
            if flag:
                ret[i] = i - stack[-1][0]
                stack.append(t[i])
        ret.reverse()
        return ret


if __name__ == "__main__":
    temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    print(Solution().dailyTemperatures(temperatures))
