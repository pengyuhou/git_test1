class Solution(object):
    def matrixReshape(self, nums, r, c):

        nums_=nums
        r_=r
        c_=c



        total = []
        for num in nums_:
            for x in num:
                total.append(x)
        if len(total)==r_*c_:

            ret = []

            for i in range(r_):
                a = []
                for j in range(c_):
                    a.append(total.pop(0))

                ret.append(a)
            return ret
        else:
            return nums_



if __name__ == '__main__':
    nums_ =[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]]
    # nums=[[1,2],[3,4]]
    r_ = 4
    c_ = 6
    s = Solution()
    print(s.matrixReshape(nums_, r_, c_))


    #
    # total = []
    # for num in nums_:
    #     for x in num:
    #         total.append(x)
    #
    # ret = []
    #
    # for i in range(r_):
    #     a = []
    #     for j in range(c_):
    #         a.append(total.pop(0))
    #
    #     ret.append(a)
    # print(ret)










