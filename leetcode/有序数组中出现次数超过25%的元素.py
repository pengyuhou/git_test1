class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        i = 0
        if len(arr)==1:
            return arr[0]
        while i <= len(arr) - 1:
            index = 1
            while arr[i] == arr[i + 1]:
                index += 1
                i += 1
                if i+1 >len(arr)-1:
                    break
            if index > 0.25 * len(arr):
                return arr[i]
            i += 1

if __name__ == '__main__':
    arr = [10,9,9]
    s=Solution()
    print(s.findSpecialInteger(arr))





