class Solution(object):
    def checkStraightLine(self, coordinates):
        l = len(coordinates)
        if l==2:
            return True
        else:
            a = coordinates[1][0]-coordinates[0][0]
            b = coordinates[1][1]-coordinates[0][1]
            if a != 0 and b != 0:
                for i in range(2,l):
                    if (coordinates[i][0]-coordinates[i-1][0])/(coordinates[i][1]-coordinates[i-1][1])!=a/b:
                        return False
                return True
            else:
                if a==0:
                    for i in range(2, l):
                        if coordinates[i][0]-coordinates[i-1][0]!=a:
                            return False
                    return True
                if b==0:
                    for i in range(2, l):
                        if coordinates[i][1]-coordinates[i-1][1]!=b:
                            return False
                    return True



if __name__ == "__main__":
    coordinates = [[0,1],[1,3],[-4,-7],[5,11]]
    print(Solution().checkStraightLine(coordinates))











