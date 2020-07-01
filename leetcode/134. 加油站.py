class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        l = len(gas)
        for i in range(l):
            now_gas = gas[i:] + gas[:i]
            now_cost = cost[i:] + cost[:i]
            amount = 0
            flag = True
            for j in range(l):
                amount += now_gas[j]
                amount -= now_cost[j]
                if amount < 0:
                    flag = False
                    break
            if flag:
                return i
        return -1



if __name__ == "__main__":
    print(Solution().canCompleteCircuit(gas  = [2,3,4],
cost = [3,4,3]))
