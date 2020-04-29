class Solution:
    def findInMountainArray(self, target, mountain_arr):
        left = 0
        right = len(mountain_arr) - 1
        while left < right:
            mid = (left + right) // 2
            mid_val = mountain_arr[mid]
            mid_left = mountain_arr[mid - 1]
            mid_right = mountain_arr[mid + 1]
            if mid_left < mid_val < mid_right:
                left = mid
            elif mid_left > mid_val > mid_right:
                right = mid
            else:
                break
            if right - left == 1:
                mid = right
                break
        left1 = 0
        right1 = mid
        left2 =None
        if mid !=len(mountain_arr)-1:
            left2 = mid+1
            right2 = len(mountain_arr)-1
        if mountain_arr[left1]==target:
            return left1
        if mountain_arr[right1]==target:
            return right1
        while right1-left1>1:
            mid = (left1 + right1) // 2
            a = mountain_arr[mid]
            if a < target:
                left1 = mid
            elif a==target:
                return mid
            else:
                right1 = mid
        if mountain_arr[left1]==target:
            return left1
        if mountain_arr[right1]==target:
            return right1
        if left2:
            if mountain_arr[left2] == target:
                return left2
            if mountain_arr[right2] == target:
                return right2
            while right2-left2>1:
                mid = (left2 + right2) // 2
                a = mountain_arr[mid]
                if a < target:
                    left2 = mid
                elif a==target:
                    return mid
                else:
                    right2 = mid
            if mountain_arr[left2] == target:
                return left2
            if mountain_arr[right2] == target:
                return right2
        return -1


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray(object):
   def get(self, index):
       """
       :type index: int
       :rtype int
       """

   def length(self):
       """
       :rtype int
       """
class Solution1(object):
    def findInMountainArray(self, target, mountain_arr):
        left = 0
        right = mountain_arr.length() - 1
        while left < right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            mid_left = mountain_arr.get(mid-1)
            mid_right = mountain_arr.get(mid+1)
            if mid_left < mid_val < mid_right:
                left = mid
            elif mid_left > mid_val > mid_right:
                right = mid
            else:
                break
            if right - left == 1:
                mid = right
                break
        left1 = 0
        right1 = mid
        left2 =None
        if mid !=mountain_arr.length()-1:
            left2 = mid+1
            right2 = mountain_arr.length()-1
        if mountain_arr.get(left1) == target:
            return left1
        if mountain_arr.get(right1) == target:
            return right1
        while right1-left1>1 :
            mid = (left1 + right1) // 2
            a = mountain_arr.get(mid)
            if a < target:
                left1 = mid
            elif a==target:
                return mid
            else:
                right1 = mid
        if mountain_arr.get(left1) == target:
            return left1
        if mountain_arr.get(right1) == target:
            return right1
        if left2:
            if mountain_arr.get(left2) == target:
                return left2
            if mountain_arr.get(right2) == target:
                return right2
            while right2-left2>1:
                mid = (left2 + right2) // 2
                a = mountain_arr.get(mid)
                if a < target:
                    left2 = mid
                elif a==target:
                    return mid
                else:
                    right2 = mid
            if mountain_arr.get(left2) == target:
                return left2
            if mountain_arr.get(right2) == target:
                return right2
        return -1


if __name__ == "__main__":
    array = [1,4,5,3,2]
    print(Solution().findInMountainArray(1, array))
