class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for i in range(n):
            i = i + 1

            if i % 3 == 0 and i % 5 == 0:
                ret.append('FizzBuzz')

            if i % 3 == 0 and i % 5 != 0:
                ret.append('Fizz')

            if i % 5 == 0 and i % 3 != 0:
                ret.append('Buzz')
            if i % 5 != 0 and i % 3 != 0:
                ret.append(str(i))
        return ret

if __name__ == '__main__':
    n = 15
    s=Solution()
    print(s.fizzBuzz(n))



