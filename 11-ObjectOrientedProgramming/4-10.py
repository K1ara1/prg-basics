class C:
    def __init__(self,points):
        self.points = points
    def m(self,n):
        count = 0
        for point in self.points:
            x,y = point
            if x > 0 and y > 0:
                count +=1
        return count >= n

def main():
    coordinates = C([[2,3],[1,8],[-6,4],[3,-7]])
    print(coordinates.m(2))
    print(coordinates.m(3))

if __name__ == '__main__':
    main()