class Solution(object):
    def findRadius(self, houses, heaters):
        houses = sorted(houses)
        heaters = sorted(heaters)
        index = 0
        ret = []
        for house in houses:
            while index < len(heaters) and house > heaters[index]:
                index += 1
            if index == 0:
                ret.append(abs(heaters[index] - house))
                continue
            if index == len(heaters):
                ret.append(abs(house - heaters[-1]))
                continue
            ret.append(min(abs(heaters[index] - house), abs(heaters[index - 1] - house)))
        return max(ret)


if __name__ == "__main__":
    print(
        Solution().findRadius([282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923],
                              [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729,
                               823378840, 143542612]))
