class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        index = 0
        while index < l:
            if arr[index]==0:
                arr.insert(index,0)
                index += 2
                continue
            index += 1
        arr[:] = arr[:l]


if __name__ == "__main__":
    nums = [1,0,2,3,0,4,5,0]
    print(Solution().duplicateZeros(nums))

