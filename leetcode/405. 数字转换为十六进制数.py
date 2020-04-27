class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return '0'
        if num<0:
            num=2**32-abs(num)

        a={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:"6",7:"7",8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        ans = ''
        while num:
            tmp = num%16
            ans += a.get(tmp)
            num = num//16
        a=list(ans)
        a.reverse()
        return ''.join(a)




if __name__ == "__main__":

    print(Solution().toHex(-1))



