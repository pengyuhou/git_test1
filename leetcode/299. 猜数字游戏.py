class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l = len(secret)
        secret = list(secret)
        guess = list(guess)
        index = 0
        bulls = 0
        while index < l:
            if secret[index]==guess[index]:
                bulls += 1
                secret.pop(index)
                guess.pop(index)
                l = len(secret)
                continue
            index += 1
        a = {}
        for i in secret:
            if i not in a.keys():
                a[i]=1
            else:
                a[i]+=1
        b={}
        for i in guess:
            if i not in b.keys():
                b[i]=1
            else:
                b[i]+=1
        cows = 0
        for i in a.keys():
            if i in b.keys():
                cows += min(a.get(i),b.get(i))
        return '{}A{}B'.format(bulls,cows)


if __name__ == "__main__":
    secret = "1807"
    guess = "7810"
    secret = "11"
    guess = "11"
    print(Solution().getHint(secret,guess))