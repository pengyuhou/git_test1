class MagicDictionary:
    def __init__(self):
        self.a = []

    def buildDict(self, x):
        for i in range(len(x)):
            self.a.append(x[i])

    def search(self, word):
        def fun(p, q):
            if len(p) != len(q):
                return False
            cnt = 0
            for i, j in zip(p, q):
                if i != j:
                    cnt += 1
                if cnt > 1:
                    return False
            if not cnt:
                return False
            return True

        for i in range(len(self.a)):
            if fun(self.a[i], word):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(['adas', 'aa'])
print(obj.a)
print(obj.search('adaf'))
