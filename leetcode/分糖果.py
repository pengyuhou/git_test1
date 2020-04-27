class Solution:
    def distributeCandies(self, candies):
        a = set(candies)
        num = len(candies) // 2
        t=len(a)

        if t >= num:
            return num
        else:
            return t

if __name__ == '__main__':
    candies = [1,1,2,2,3,3]
    a=set(candies)
    num=len(candies)//2

    if len(a) >= num:
        print(num)
    else:
        print(len(a))




