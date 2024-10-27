def f(n1,n2,n3):
   
   if n1 < 0 or n2 < 0 or n3 < 0:
      return True
   else:
      return False
result1 = int(input('Enter n1: '))
result2 = int(input('Enter n2: '))
result3 = int(input('Enter n3: '))
print(f(result1,result2,result3))