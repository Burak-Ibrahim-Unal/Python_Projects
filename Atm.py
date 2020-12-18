print("""
##############################
Atm Machine
##############################
1-Balance Query
2-Deposit
3-Withdraw money
##############################
Press "q" to exit...
##############################
""")
balance=1000
while True:
    process=input("Please select process:")
    if process == "q":
        print("Always welcome...")
        break
    elif process=="1":
        print("Your balance is {} TL".format(balance))
    elif process=="2":
        amount=int(input("Please type amount to deposit:"))
        balance+=amount
    elif process =="3":
        amount=int(input("Please type amount to withdraw:"))
        if amount > balance:
            print("Not enough balance...")
            continue
        balance=balance-amount
    else:
        print("Unvalid process...")

