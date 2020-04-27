class A(object):
    def merge_sort(self, a):
        """
        分治法
        """
        l = len(a)
        if l == 1:
            return a
        mid = l // 2
        ret = []
        left = self.merge_sort(a[:mid])
        right = self.merge_sort(a[mid:])

        index1 = 0
        index2 = 0
        while index1 < len(left) and index2 < len(right):
            if left[index1] < right[index2]:
                ret.append(left[index1])
                index1 += 1
            else:
                ret.append(right[index2])
                index2 += 1
        ret += left[index1:]
        ret += right[index2:]
        return ret


if __name__ == '__main__':
    a = [1, 2, 1, 45, 67, 1, 3, 4, 5, 7, 9, 30, 4]

    # a=[1,10,11,2,6,9]
    print(A().merge_sort(a))
