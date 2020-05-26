class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        import random
        while True:
            xr = random.uniform(self.x_center - self.radius, self.x_center + self.radius)
            yr = random.uniform(self.y_center - self.radius, self.y_center + self.radius)
            if (xr - self.x_center) ** 2 + (yr - self.y_center) ** 2 < self.radius ** 2:
                return [xr, yr]


# Your Solution object will be instantiated and called as such:
obj = Solution(1, 2, 3)
param_1 = obj.randPoint()
print(param_1)

import random

print(random.uniform(8, 9))
