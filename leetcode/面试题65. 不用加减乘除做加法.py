class Solution:
    def add(self, a: int, b: int) -> int:
        return sum([a,b])



if __name__ == '__main__':
    a = 14
    b = -4
    a = bin(a)
    b = bin(b)
    a = list(a)
    b = list(b)
    print(a)
    print(b)
    # if len(a)<len(b):
    #     for i in range(len(b)-len(a)):
    #         a.insert(0,'0')
    # if len(a)>len(b):
    #     for i in range(len(a)-len(b)):
    #         b.insert(0,'0')
    # a = [int(x) for x in a]
    # b = [int(x) for x in b]
    # print(a)
    # print(b)
    # l = len(a)
    # index1 = l-1
    # index2 = l-1
    # ret = []
    # tmp = 0
    # while index1>=0:
    #     ret.append(a[index1] ^ b[index2] ^ tmp)
    #     if (a[index1] and b[index2])or ((a[index1] or b[index1] )and tmp):
    #         tmp = 1
    #     else:
    #         tmp = 0
    #     index1 -= 1
    #     index2 -= 1
    # if tmp:
    #     ret.append(tmp)
    # ret.reverse()
    # print(ret)






























