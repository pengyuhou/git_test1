class Solution(object):
    def arrayRankTransform(self, arr):
        arr1=arr.copy()
        arr1=list(set(arr1))
        arr1.sort()
        a = {}
        for i in range(len(arr1)):
            if arr1[i] not in a.keys():
                a[arr1[i]]=i+1
        for i in range(len(arr)):
            arr[i]=a[arr[i]]
        return arr

if __name__ == "__main__":
    arr = [100, 100, 100]
    # arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    print(Solution().arrayRankTransform(arr))


