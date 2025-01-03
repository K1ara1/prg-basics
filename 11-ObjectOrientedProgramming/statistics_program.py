import statistics
class Statistic():
    def __init__(self,*args):
        self.numbers = list(args)
    def display(self):
        print(", ".join(map(str, self.numbers)))
    def greatest(self):
        print(max(self.numbers))
    def smallest(self):
        print(min(self.numbers))
    def arithmetic_mean(self):
        print((sum(self.numbers))/(len(self.numbers)))
    def median(self):
        print(statistics.median(self.numbers))

def main():
    my_numbers = Statistic(12, 37, 6, 9, 17)
    my_numbers.display()
    my_numbers.greatest()
    my_numbers.smallest()
    my_numbers.arithmetic_mean()
    my_numbers.median()
if __name__ == '__main__':
    main()