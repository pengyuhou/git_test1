class Solution(object):
    def findRestaurant(self, list1, list2):
        a = {}
        b = {}
        l1 = len(list1)
        l2 = len(list2)
        for i in range(l1):
            a[list1[i]] = i
        for i in range(l2):
            b[list2[i]] = i
        ret = list(set(list1) & set(list2))
        res = sorted(ret,key= lambda x:a[x]+b[x])
        c = a[res[0]]+b[res[0]]
        ret=[]
        for i in res:
            if a[i]+b[i]==c:
                ret.append(i)
        return ret







if __name__ == "__main__":
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    list2 = ["KFC", "Shogun", "Burger King"]

    list1=["Shogun","Tapioca Express","Burger King","KFC"]
    list2=["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
    print(Solution().findRestaurant(list1,list2))

















