class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        queue = {n}
        cnt = 0
        while queue:
            cnt += 1
            next = set()
            for i in queue:
                for num in nums:
                    if i - num > 0:
                        next.add(i - num)
                    if i - num == 0:
                        return cnt
            queue = next
        return 0


print(Solution().numSquares(7168))
