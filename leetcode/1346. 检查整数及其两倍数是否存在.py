class Solution(object):
    def checkIfExist(self, arr):
        l = len(arr)
        for i in range(l-1):
            for j in range(i+1,l):
                if arr[i]==2*arr[j] or arr[i]==arr[j]/2:
                    return True
        return False


if __name__ == "__main__":
    arr = [7, 1, 14, 11]
    arr = [3, 1, 7, 11]
    arr = [-2,0,10,-19,4,6,-8]
    print(Solution().checkIfExist(arr))
