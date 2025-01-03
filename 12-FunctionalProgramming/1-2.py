n1 = int(input('x:'))
n2 = int(input('y:'))

mean = lambda x,y: (x+y)/2

result = mean(n1,n2)
print(f"The arithmetic mean of the numbers {n1} and {n2} is {result}")