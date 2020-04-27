class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        a = list(range(left, right + 1))
        ret = []
        for i in a:
            flag = False
            if '0' in str(i):
                flag = True
            if not flag:
                num = i
                index = 0
                while i > 0:

                    res = i % 10
                    if num % res == 0:
                        index += 1
                    i = i // 10
                if index == len(str(num)):
                    ret.append(num)
        return ret

if __name__ == '__main__':
    left=1
    right=22













