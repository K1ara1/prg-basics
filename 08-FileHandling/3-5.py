import re

username = input('Enter your username: ')
password = input('Enter your password: ')

username_pattern = '[a-z]{6,}'
password_pattern = '[a-zA-Z0-9_]{8,}'

username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

if username_match and password_match:
   print(username, password, 'Correct')
else:
   print('Incorrect')