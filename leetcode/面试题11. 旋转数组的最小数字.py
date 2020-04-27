# 直接遍历
class Solution1(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        for i in range(len(numbers)-1):
            if numbers[i]>numbers[i+1]:
                return numbers[i+1]
        return numbers[0]

# 二分查找
class Solution(object):
    def findMin(self, numbers):
        l = len(numbers)
        index1 = 0
        index2 = l-1
        while index2-index1>1:
            mid = (index1 + index2)//2
            if numbers[index1]>numbers[mid]:
                index2 = mid
                continue

            if numbers[index2] < numbers[mid]:
                index1 = mid
                continue
            if numbers[index1]==numbers[mid] and numbers[index2]==numbers[mid]:
                if all([i==numbers[mid] for i in numbers[index1:mid]]):
                    index1 =mid
                    continue
                else:
                    index2 = mid
                    continue
            return numbers[0]
        return min(numbers[index1],numbers[index2])




if __name__ == "__main__":
    nums=[9,11,1,3,5,8]
    nums= [2,1,5]
    nums =[1,3,5]
    # nums =[3,3,3,3,3,3,3,3,1,3]
    nums= [3, 3, 1, 3]
    nums = [10, 1,10, 10, 10, 10]
    nums = [-9,-9,-9,-8,-8,-7,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-5,-5,-4,-4,-4,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,0,0,0,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5,5,6,6,6,7,7,7,7,7,8,9,9,9,10,10,10,10,10,10,10,-10,-9,-9,-9,-9]

    # print(Solution1().minArray(nums))
    print(Solution().findMin(nums))



