class Solution(object):
    def sortByBits(self, arr):
        arr.sort()
        res = sorted(arr, key=lambda x: bin(x).count('1'))
        return res


if __name__ == "__main__":
    arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    # arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # arr = [10000, 10000]









