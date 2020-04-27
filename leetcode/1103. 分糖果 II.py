class Solution(object):
    def distributeCandies(self, candies, num_people):
        ret = [0] * num_people
        num_can = 1
        index = 0
        candies -= num_can
        while candies > 0:
            ret[index % num_people] += num_can
            index += 1
            num_can += 1
            candies -= num_can
            if candies <= 0:
                ret[index % num_people] += num_can + candies
                break
        return ret

if __name__ == "__main__":
    candies = 10
    num_people = 3
    print(Solution().distributeCandies(candies,num_people))




















