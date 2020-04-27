class Solution(object):
    def replaceWords(self, di, sentence):
        a={}
        res=sentence.split()
        for element in di:
            if element[0] in a.keys():
                a[element[0]].append(element)
            else:
                a[element[0]]=[element]
        for x in a.values():
            a[x[0][0]]=sorted(x,key=lambda t:len(t))
        for i in range(len(res)):
            if res[i][0] in a.keys():
                l = len(a[res[i][0]])
                index = 0
                while index<l:
                    if a[res[i][0]][index] in res[i][:len(a[res[i][0]][index])]:
                        res[i] = a[res[i][0]][index]
                        break
                    index += 1
        return ' '.join(res)




if __name__ =="__main__":
    # print('ae' in 'anlrixkeqaexh')
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(Solution().replaceWords(dict,sentence))


