class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        a = {}
        licensePlate = licensePlate.lower()
        for i in range(len(licensePlate)):
            if licensePlate[i].isalpha():
                if licensePlate[i] not in a.keys():

                    a[licensePlate[i]] = 1
                else:
                    a[licensePlate[i]] += 1
        ret = []
        for word in words:
            flag = True
            for k, v in a.items():
                if word.count(k) < v:
                    flag = False
                    break
            if flag:
                ret.append(word)
        return min(ret, key=lambda x: len(x))

if __name__ == "__main__":
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    print(Solution().shortestCompletingWord(licensePlate,words))






















