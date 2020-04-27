class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l = len(arr)
        max_ = 0
        for i in range(l - 1, -1, -1):
            if i == l - 1:
                max_ = arr[i]
                arr[i] = -1
            else:
                t = arr[i]
                arr[i] = max_
                if t > max_:
                    max_ = t
        return arr

if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    S=Solution()
    print(S.replaceElements(arr))


    # print(arr)





