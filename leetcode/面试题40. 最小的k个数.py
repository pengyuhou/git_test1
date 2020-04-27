class Solution:
    def getLeastNumbers(self, arr, k) :
        arr = sorted(arr)
        return arr[:k]


if __name__ == "__main__":
    arr = [0, 1, 2, 1]
    k = 1
    print(Solution().getLeastNumbers(arr,k))












