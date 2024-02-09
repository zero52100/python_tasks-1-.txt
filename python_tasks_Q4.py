"""
Q4.Python program to check the number taken as an input is even or odd,print invalide input if user enters anything other than integers
"""
try:
    num=int(input("Enter the number"))

    if num%2==0:
        print("Enter number is EVEN")
    else:
        print("Enter number is ODD")
except ValueError:
    print("Invalid input , Please enter an integer.")

