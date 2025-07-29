accounts = {101:1000,102:2000,103:5000}

def menu():
    print("Menu")
    print("1.Check balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit to Main Menu")

while True:
    print("Welcome to Bank")
    ch = int(input("Enter the account number (0 to exit):"))
    if ch==0:
        exit(0)
    elif ch not in accounts:
        print("Invalid account number!")
        continue
    else:
        acc=ch  
    while True:
        menu()
        choice=int(input("Enter your choice: "))
        if choice==1:
            print("Current Balance:", accounts[acc])
        elif choice == 2:
            amt = int(input("Enter amount to deposit: "))
            accounts[acc]+=amt
            print("Amount Deposited. New Balance:", accounts[acc])
        elif choice==3:
            amt = int(input("Enter amount to withdraw: "))
            if amt>accounts[acc]:
                print("balance is less")
            else:
                accounts[acc]-=amt
                print("Amount Withdrawn", accounts[acc])
        elif choice==4:
            print("Exiting to main menu")
            break
        else:
            print("Invalid choice! Try again.")
