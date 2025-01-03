class Bank():
    def __init__(self,account):
        self.account = account
        self.balance = 0
    def deposit(self,amount_deposited):
        self.balance += amount_deposited
    def withdraw(self,amount_withdrawed):
        if amount_withdrawed <= self.balance:
            self.balance -= amount_withdrawed
        else:
            print('Insufficient funds on the account.')
    def status(self):
        print(f'Bank account No: {self.account}')
        print(f'Balance PLN: {self.balance}')

def main():
    my_bank = Bank('12 3456 5555 9090 1111 0000 7722')
    my_bank.status()
    my_bank.deposit(25.30)
    my_bank.status()
    my_bank.withdraw(31.70)
    my_bank.status()
    my_bank.withdraw(14)
    my_bank.status()
if __name__ == '__main__':
    main()