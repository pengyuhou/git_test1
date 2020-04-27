class Solution(object):
    def numberOfSteps (self, num):
        count = 0
        while num:
            if not num % 2:
                num = num // 2
                count += 1
            else:
                num -= 1
                count += 1
        return count


if __name__ == "__main__":
    num = 123






