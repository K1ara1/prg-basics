x = int(input('Enter x: '))
y = int(input('Enter y: '))

if x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system.')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system.')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system.')
elif x > 0 and y < 0:
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system.')
elif x == 0 and y != 0:
    print(f'Point P({x},{y}) is on the Y axis.')
elif x != 0 and y == 0:
    print(f'Point P({x},{y}) is on the X axis.')
else:
    print(f'It is point P({x},{y}) of the coordinate system.')
