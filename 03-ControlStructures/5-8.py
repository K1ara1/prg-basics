balance = 1000  
pin = '1111'

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print(f"Your current pin is: {pin}")
    elif choice == '5':
        pin = input("Enter new PIN: ")
        if pin.isdigit() == True:
            print(f"Your new PIN is: {pin}")
        else:
            print(f'Incorrect PIN.')
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break 
    else:
        print("Invalid option. Please try again.")