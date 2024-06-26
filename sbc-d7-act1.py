import random

accounts = {}

print("Welcome to Diana's ATM Machine")

def create_account():
    global accounts
    cusname = input("Enter Name: ")
    acc = random.randint(1000, 9999)
    accounts[acc] = (cusname, 1000)  
    print(f"Account created successfully. Your account number is: {acc}") 

def login():
    acc = int(input("Enter your account number: "))
    if acc in accounts:
        cusname, _ = accounts[acc]
        print(f"Welcome {cusname}!")
        return acc
    else:
        print("Account not found.")
        return None

def delete_account(acc):
    global accounts
    del accounts[acc]
    print("Account deleted successfully.")

def details(acc):
    cusname, balance = accounts[acc]
    print("Account Number:", acc)
    print("Customer Name:", cusname)
    print("Current Balance:", balance)

def deposit(acc, amount):
    global accounts
    accounts[acc] = (accounts[acc][0], accounts[acc][1] + amount)
    print(f"Deposited {amount}.")
    check_balance(acc)

def withdraw(acc, amount):
    global accounts
    if amount > accounts[acc][1]:
        print("Insufficient balance.")
    else:
        accounts[acc] = (accounts[acc][0], accounts[acc][1] - amount)
        print(f"Withdraw {amount}.")
        check_balance(acc)

def check_balance(acc):
    _, balance = accounts[acc]
    print("Current balance:", balance)

ch1 = "y"
while ch1 == "y":
    print("1. Create Account\n2. Login\n3. Exit")
    ch = int(input("Select any option: "))
    
    if ch == 1:
        create_account()
        
    elif ch == 2:
        acc = login()
        if acc:
            while True:
                print("\n1. Details\n2. Withdraw\n3. Deposit\n4. Check Balance\n5. Delete Account\n6. Logout")
                transaction_choice = int(input("Select any transaction option: "))
                
                if transaction_choice == 1:
                    details(acc)
                elif transaction_choice == 2:
                    amnt = int(input("Enter amount to withdraw: "))
                    withdraw(acc, amnt)
                elif transaction_choice == 3:
                    amnt = int(input("Enter amount to deposit: "))
                    deposit(acc, amnt)
                elif transaction_choice == 4:
                    check_balance(acc)
                elif transaction_choice == 5:
                    delete_account(acc)
                    break
                elif transaction_choice == 6:
                    break
                else:
                    print("Invalid option. Please choose again.")
        else:
            print("Login failed. Please try again.")
    
    elif ch == 3:
        break
    
    ch1 = input("Do you want to continue (y/n)? ").lower()

print("Thank you for using Diana's ATM Machine.")
