class Solution:
    def isOneBitCharacter(self, bits ):
        index = 0
        l = len(bits)

        while index <= l - 1:
            if bits[index]:
                flag = False
                index += 2

            else:
                flag = True
                index += 1
        return flag


if __name__ == "__main__":
    bits = [1, 1, 1, 0]
    print(Solution().isOneBitCharacter(bits))







