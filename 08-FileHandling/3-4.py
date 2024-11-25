import re

email_file = 'report.txt'

with open(email_file, 'r')as file:
   email = file.read()

pattern = '\d+'

amounts = re.findall(pattern, email)

count = 0
for amount in amounts:
   count += int(amount)

print(count)