class Solution(object):
    def maxArea(self, height):
        l=len(height)
        index1 = 0
        index2 = l -1
        ret = []
        while index1<index2:
            ret.append(min(height[index1],height[index2])*(index2-index1))
            if height[index1] < height[index2]:
                index1 += 1
            else:
                index2 -= 1
        return max(ret)




if __name__ == "__main__":
    nums = [9,1]
    print(Solution().maxArea(nums))

