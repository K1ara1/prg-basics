import keyboards

first_name = keyboards.input_string('Enter name: ')
last_name = keyboards.input_string('Enter surname: ')
age = keyboards.input_integer('Enter age: ')
salary = keyboards.input_real('Enter salary: ')
is_salary_hidden = keyboards.input_boolean('Hide salary? (y/n)')

print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Surname:', last_name)
print('Age:', age)
if is_salary_hidden == 'n':
    print('Salary:', salary)