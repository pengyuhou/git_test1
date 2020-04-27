class Solution:
    def binaryGap(self, N: int) -> int:
        res = bin(N)[2:]
        index = 0
        l = len(res)
        distance = None
        while index < l:
            if res[index] == '1' and distance is None:
                distance = 0
                tmp = index
                index += 1
            elif res[index] == '1' and distance is not None:
                if index-tmp>distance:
                    distance = index-tmp
                tmp = index
                index += 1
            else:
                index += 1
        return distance

if __name__ == '__main__':
    print(Solution().binaryGap(8))
