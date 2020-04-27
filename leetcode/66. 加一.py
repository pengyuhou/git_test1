class Solution(object):
    def plusOne(self, digits):
        return [int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]

if __name__ == "__main__":
    print(Solution().plusOne([9]))