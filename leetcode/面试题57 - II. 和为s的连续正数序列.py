class Solution(object):
    def findContinuousSequence(self, target):
        index1 = 1
        ret = []
        while index1 < target - 1:
            count = index1
            index2 = index1 + 1
            while count < target:
                count += index2
                index2 += 1
            if count == target:
                ret.append(list(range(index1, index2)))
            index1 += 1
        return ret

if __name__ == "__main__":
    target = 15
    print(Solution().findContinuousSequence(target))



