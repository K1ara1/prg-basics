pin = '0805'

for i in range(3) :
    code = input('Enter PIN: ')
    if code == pin:
        print('Correct')
        break
    else:
        print('Incorrect')
print('Sorry, your payment card has been blocked.')
