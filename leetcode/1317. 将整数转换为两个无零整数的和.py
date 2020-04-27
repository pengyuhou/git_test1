class Solution:
    def getNoZeroIntegers(self, n: int) :
        index1 = 1
        index2 = n - 1

        while index1 <= index2:


            if '0' not in str(index1) and '0' not in str(index2):

                return [index1,index2]

            index1 += 1
            index2 -= 1

if __name__ == "__main__":

    n = 9998
    print(Solution().getNoZeroIntegers(n))





