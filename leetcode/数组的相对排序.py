class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        ret = []
        res = []
        for x in arr1:
            if x not in arr2:
                res.append(x)
        res = sorted(res)
        for i in arr2:
            for j in arr1:
                if i == j:
                    ret.append(i)
        return ret+res


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 19, 9, 2, 7]
    arr2 = [2, 1, 4, 3, 9, 6]

    s=Solution()
    print(s.relativeSortArray(arr1,arr2))





