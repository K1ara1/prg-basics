class C:
    def __init__(self, sector_data):
        self.sectors = sector_data

    def m1(self, s, n):
        self.sectors[s] = n

    def m2(self, s):
        total_fans = 0
        for sector in s:
            if sector in self.sectors:
                total_fans += self.sectors[sector]
        return total_fans

def main():
    stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})
    stadium.m1("G", 130)
    print(stadium.m2("GD")) 
    print(stadium.m2("KEJ")) 

if __name__ == "__main__":
    main()