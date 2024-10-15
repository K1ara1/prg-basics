basic_salary = 5000
total_salary = 0
is_bonus = input("Enter if you recieve a bonus: (Y/N)")
bonus = " "

if is_bonus == "Y":
    bonus = int(input("Enter your bonus: "))
    total_salary = basic_salary*bonus/100 + basic_salary
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')