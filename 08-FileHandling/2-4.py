employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

job_title = 'Software Engineer'

with open(employees_file, 'r') as file:
   with open(position_file, 'w') as filex:
      for line in file:
         if job_title in line:
            filex.write(line)