#Bank Management System
#Author : Akhil Jobbi

class BankAccount:
    bank_name = "STATE BANK OF INDIA"
    interest_rate=4
    def __init__(self,account_holder,account_number,balance,account_type,pin):
        self.account_holder =account_holder
        self.account_number =account_number 
        self.balance= balance
        self.account_type= account_type
        self.pin = pin
        self.last_transaction = None

    def deposit(self,deposit_amount):

        if deposit_amount>0:
            self.balance += deposit_amount
            self.last_transaction = f"Deposited Rs.{deposit_amount}"
            print(f"{deposit_amount} successfully deposited \n The current balance is {self.balance}")
        else :
            print("Invalid Input")

    def withdraw(self,withdraw_amount,pin):
        if withdraw_amount<=0:
            print("Enter valid amount")
            return
        if withdraw_amount>self.balance:
            print("Insufficient balance")
            return
        if not self.verify_pin(pin):
            return
        
        self.balance -= withdraw_amount
        self.last_transaction = f"Withdrawn Rs.{withdraw_amount}"
        print(f"{withdraw_amount} successfully withdrawn \n The current balance is {self.balance}")

            
                
            

    def check_balance(self,pin):
        if not self.verify_pin(pin):
            return

        print(f"The Bank balance is {self.balance}")

    def change_pin(self,old_pin,new_pin):
        if not self.verify_pin(old_pin):
            return
            
        if new_pin == old_pin:
            print("New pin can't be same as the old one")
            return
        if new_pin>=1000 and new_pin<=9999:
            self.pin=new_pin
            print("Pin was successfully changed")
        else:
            print("Invalid format.The pin should be 4 digits.")

    def display_account(self,pin):
        if not self.verify_pin(pin):
            return

        print(f"Account Holder : {self.account_holder}\nAccount Number : {self.account_number}\nAccount Type : {self.account_type}\nBank Name : {BankAccount.bank_name}")
    
    def add_interest(self,years,pin):
        if not self.verify_pin(pin):
           return

        if self.account_type != "Savings account" :
            print("Interest only for savings account")
            return
        interest = (BankAccount.interest_rate/100*self.balance)*years
        self.balance+=interest
        self.last_transaction = f"Interest added: Rs{interest}"
        print(f"The balance with the added interest : {self.balance}")

    def verify_pin(self,pin):
        if pin != self.pin:
            print("Incorrect Pin")
            return False
        else:
            return True


accounts=[]

def find_account(Accountnumber):
    for account in accounts:
        if account.account_number == Accountnumber: 
            return account
    return None    



while True:
    print("==================================================================\n")
    print("STATE BANK OF INDIA")
    print("==================================================================\n")
    print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Display Account\n6. Change PIN\n7. Add Interest \n8. Exit")
    choice = int(input("Enter the choice :\n"))

    if choice == 1:
        account_holder = input("Enter the name of the account holder : ")
        account_number = int(input("Enter the account number : "))
        account = find_account(account_number)
        if account is not None:
            print("Account number already exists")
            continue
        initial_balance = float(input("Enter the initial balance : "))
        account_type=input("Enter the account type : ")
        pin=int(input("Enter the pin : "))
        new_account= BankAccount(account_holder,account_number,initial_balance,account_type,pin)
        print("Account created successfully")
        accounts.append(new_account)

    elif choice == 2 :
        account_number = int(input("Enter the account number : "))
        account = find_account(account_number)
        if account is None:
            print("Account does not exist ")
            continue
        deposit_amount=float(input("Enter the deposit amount : "))
        account.deposit(deposit_amount)

    elif choice == 3:
        account_number = int(input("Enter the account number : "))
        account = find_account(account_number)
        if account is None:
            print("Account does not exist ")
            continue
        withdrawal_amount = float(input("Enter the withdrawal amount : "))
        pin=int(input("Enter the PIN : "))
        account.withdraw(withdrawal_amount,pin)

    elif choice == 4:
        account_number = int(input("Enter the account number : "))
        account = find_account(account_number)
        if account is None:
            print("Account does not exist ")
            continue
        pin=int(input("Enter the PIN : "))
        account.check_balance(pin)

    elif choice == 5:
        account_number = int(input("Enter the account number : "))
        account = find_account(account_number)
        if account is None:
            print("Account does not exist ")
            continue
        pin=int(input("Enter the PIN : "))
        account.display_account(pin)

    elif choice == 6:
        account_number = int(input("Enter the account number : "))
        account = find_account(account_number)
        if account is None:
            print("Account does not exist ")
            continue
        old_pin=int(input("Enter the old pin : "))
        new_pin=int(input("Enter the new pin : "))
        account.change_pin(old_pin,new_pin)

    elif choice == 7:
        account_number = int(input("Enter the account number : "))
        account = find_account(account_number)
        if account is None:
            print("Account does not exist ")
            continue
        pin=int(input("Enter the PIN : "))
        years=float(input("Enter the number of years since account was opened : "))
        account.add_interest(years,pin)

    elif choice == 8:
        print("EXITING.............")
        break
    else:
        print("Enter a valid choice : ")
        continue





