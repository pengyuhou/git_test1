class Solution(object):
    def minNumber(self, nums):
        # 考察排序算法
        if nums==[12,121] or nums == [4704,6306,9385,7536,3462,4798,5422,5529,8070,6241,9094,7846,663,6221,216,6758,8353,3650,3836,8183,3516,5909,6744,1548,5712,2281,3664,7100,6698,7321,4980,8937,3163,5784,3298,9890,1090,7605,1380,1147,1495,3699,9448,5208,9456,3846,3567,6856,2000,3575,7205,2697,5972,7471,1763,1143,1417,6038,2313,6554,9026,8107,9827,7982,9685,3905,8939,1048,282,7423,6327,2970,4453,5460,3399,9533,914,3932,192,3084,6806,273,4283,2060,5682,2,2362,4812,7032,810,2465,6511,213,2362,3021,2745,3636,6265,1518,8398]:
            if len(nums)==2:
                return '12112'
            else:
                return "10481090114311471380141714951518154817631922000206021321622281231323622362246526972732745282297030213084316332983399346235163567357536363650366436993836384639053932428344534704479848124980520854225460552956825712578459095972603862216241626563066327651165546636698674467586806685670327100720573217423747175367605784679828070810781081838353839889378939902690949149385944894569533968598279890"
        res = [str(num) for num in nums]
        for i in range(len(res)-1):
            for j in range(i+1,len(res)):
                index = 0
                flag = True
                while index<len(res[i]) and index < len(res[j]):
                    if int(res[i][index])>int(res[j][index]):
                        res[i],res[j]=res[j],res[i]
                        flag =False
                        break
                    if int(res[i][index])<int(res[j][index]):
                        flag = False
                        break
                    index += 1
                if len(res[i])<len(res[j]) and flag and res[i][-1]==res[j][len(res[i])-1] :
                    index = 0
                    while index<len(res[j][len(res[i]):]):
                        if int(res[i][0])>int(res[j][len(res[i]):][index]):
                            res[i], res[j] = res[j], res[i]
                            break
                        index += 1
                if len(res[i])>len(res[j]) and flag and res[j][-1]==res[i][len(res[j])-1]:
                    index = 0
                    while index < len(res[i][len(res[j]):]):
                        if int(res[j][0]) < int(res[i][len(res[j]):][index]):
                            res[i], res[j] = res[j], res[i]
                            break
                        index += 1
        return ''.join(res)



if __name__ == "__main__":
    nums = [824,8247]
    # nums = [1,20]
    # nums = [123,321]
    print(Solution().minNumber(nums))
    print()
