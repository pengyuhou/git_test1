class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count = 0
        for num in range(L, R + 1):
            a = list(bin(num))
            x = a.count('1')
            flag = False
            if x == 1 or x == 0:
                continue
            for i in range(2, x):
                if not x % i:
                    flag = True
                    break
            if not flag:
                count += 1
        return count

if __name__ == "__main__":
    L = 6
    R = 10
    count=0

    for num in range(L,R+1):
        a=list(bin(num))
        x=a.count('1')
        flag=False
        if x==1 or x==0:
            continue
        for i in range(2,x):
            if not x%i:
                flag=True
                break
        if not flag:
            count += 1
    print(count)












