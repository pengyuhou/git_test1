# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, identify):
        from collections import deque
        d = deque()
        def fun(idf):
            for i in range(len(employees)):
                if employees[i].id == idf:
                    return employees[i]
        d.append(fun(identify))
        cnt = 0
        while d:
            a = d.popleft()
            cnt += a.importance
            for i in a.subordinates:
                d.append(fun(i))
        return cnt









