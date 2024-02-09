"""
Q2   Python Program to replicate bank transaction: min balance 500, ask user to the amount to withdraw, 
     print the balance amount after withdrawal, if user enters an amount greater than balance: print:: insufficient balance. 
     if balance is below 500 print an alert message : your account balance is "available_balance", Please  keep your account balance above Rs.500 to avoid unwanted charges.
"""

min_balance=500
available_balance=float(input("Enter the initial account balance:"))
withdraw_amount=float(input("Enter the amount to withdraw:"))
if withdraw_amount > available_balance:
    print("Insufficient balance !")
else:
    
    new_available_balance = available_balance - withdraw_amount
    if new_available_balance < min_balance:
        print(f"Your account balance is {new_available_balance}. Please keep your account balance above Rs.500 to avoid unwanted charges.")
    else:
        print(f"Withdrawal successful. Your new balance is: {new_available_balance}")