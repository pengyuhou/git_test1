class Solution:
    def mySqrt(self, x: int) -> int:
        if x== 2 or x==1:
            return 1
        cur=x//2
        left=1
        right=x
        while True:

            while cur**2 > x:
                right=cur
                cur=(left+right)//2
                if cur==right:
                    return cur

            while cur**2 < x:
                left=cur
                cur=(left+right)//2
                if cur==left :
                    return cur

            if cur**2 == x:
                return cur






if __name__ =="__main__":
    n=183692038

    print(Solution().mySqrt(n))

