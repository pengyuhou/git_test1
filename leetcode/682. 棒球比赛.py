class Solution:
    def calPoints(self, ops) :
        l = len(ops)
        index = 0
        while index <= l - 1:
            if ops[index] != 'C' and ops[index] != 'D' and ops[index] != '+':
                index += 1
                continue
            if ops[index] == 'C':
                cur=1
                if ops[index-cur]=='C':

                    while  ops[index-cur]=='C' or ops[index-cur]==None:
                        cur += 1
                    ops[index - cur]=None
                    index += 1
                    continue
                else:
                    ops[index-cur]=None
                    index += 1
                    continue

            if ops[index] == 'D':
                if ops[index - 1]!= 'C':
                    ops[index] = str(2 * int(ops[index - 1]))
                    index += 1
                    continue
                else:
                    cur=3
                    while ops[index-cur] =='C' or ops[index-cur] ==None:
                        cur += 1
                    ops[index] = str(2 * int(ops[index - cur]))
                    index += 1
                    continue

            if ops[index] == '+':
                cur1 = 1
                ret = []
                while len(ret) < 2:
                    if ops[index - cur1]!=None and ops[index - cur1] != 'C':
                        ret.append(int(ops[index - cur1]))
                        cur1 += 1
                    else:
                        cur1 += 1
                ops[index] = str(sum(ret))
                index += 1
                continue

        return sum([int(i) for i in ops if i!=None and i!='C' ])

if __name__ ==  "__main__":
    # ops = ["-60","D","-36","30","13","C","C","-33","53","79"]
    ops=["11482","C","-16664","-8297","+","D","19136","D","-10145","D","21701","+","20987","C","D","C","-17917","17151","273","C","19619","18087","D","-2040","-28447","-16785","-29805","C","C","D","-534","5898","-19769","13074","-17065","22139","28093","D","+","-22768","9116","C","C","-2035","D","25271","-8145","16575","+","-17996"]
    # ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(Solution().calPoints(ops))
    # r=['5', None, 'C', '10', '15']




    # print(count)





















