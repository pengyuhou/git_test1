class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                n-=1
                if n==0:
                    return True
            return False
        for i in range(len(flowerbed)):
            if i==0:
                if flowerbed[i]==0:
                    if flowerbed[i+1]==0:
                        flowerbed[i] = 1
                        n -= 1
                        if n == 0:
                            return True
                continue
            if i==len(flowerbed)-1:
                if flowerbed[i]==0:
                    if flowerbed[i-1]==0:
                        flowerbed[i]=1
                        n-=1
                        if n==0:
                            return True
                    continue
            if 0<i<len(flowerbed)-1:
                if flowerbed[i]==0:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        flowerbed[i] = 1
                        n -= 1
                        if n==0:
                            return True
                    continue
        return False


if __name__ == "__main__":
    flowerbed = [1]
    n = 1
    print(Solution().canPlaceFlowers(flowerbed,n))



