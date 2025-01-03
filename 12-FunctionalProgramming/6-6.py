names = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]
full_name = list(map(lambda name: f"{name[0].upper()}, {name[1]}",names))
for name in full_name:
    print(name)