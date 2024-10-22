def triangle_area(a,b,c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

triangle = triangle_area(a,b,c)

print(f'The area of a triangle with a sides of {a}, {b}, {c} is {triangle}')