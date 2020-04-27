class Solution:
    def findWords(self, words):
        a={
            1:['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P'],
            2:['A','S','D','F','G','H','J','K','L','a','s','d','f','g','h','j','k','l'],
            3:['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
        }
        ret = []
        for word in words:
            if word[0] in a[1]:
                flag =True
                for i in word:
                    if i not in a[1]:
                        flag=False
                        break
                if flag:
                    ret.append(word)
            if word[0] in a[2]:
                flag =True
                for i in word:
                    if i not in a[2]:
                        flag=False
                        break
                if flag:
                    ret.append(word)
            if word[0] in a[3]:
                flag =True
                for i in word:
                    if i not in a[3]:
                        flag=False
                        break
                if flag:
                    ret.append(word)
        return ret

if __name__ == "__main__":
    words =   ["Hello", "Alaska", "Dad", "Peace"]
    print(Solution().findWords(words))


