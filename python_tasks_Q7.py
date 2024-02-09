"""
Q7.Python program to print the multiplication table of any number (number should be taken as input 
   and user decides the end limit of the table)
"""
try:
    num=int(input("Enter the number to print the multiplication table : "))
    limit=int(input("Enter end limit of the  multiplication table : "))
    for i in range(1,limit+1):
        print(num,"*",i,"=",i*num)
except ValueError:
    print("Invalid input !")








