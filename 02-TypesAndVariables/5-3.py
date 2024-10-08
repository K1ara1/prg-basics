a = input("a=")
b = input("b=")
c = input("c=")
a1 = int(a)
b1 = int(b)
c1 = int(c)
cuboid_volume = a1*b1*c1
cuboid_surface_area = a1*b1*2+a1*c1*2+b1*c1*2
print(f"The volume of the cuboid with the sides {a1} {b1} {c1} is {cuboid_volume}")
print (f"The surface area of the cuboid with the sides {a1} {b1} {c1} is {cuboid_surface_area}")