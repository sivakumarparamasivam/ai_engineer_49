

class BankAccount:

    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type
        ################
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if(self.balance < amount):
            print('In-sufficient Balance')
        else:    
            self.balance -= amount

    def displayBalance(self):
        print(f"Account Holder Name: {self.account_holder}")
        print(f"Balance Amount: {self.balance}")


if __name__ == "__main__":
    print("I'm Running!")
    bank_account = BankAccount("Sivakumar", 100, "Savings")
    bank_account.deposit(200)
    bank_account.withdraw(400)
    bank_account.displayBalance()






