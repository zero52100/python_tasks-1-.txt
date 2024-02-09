"""
Q9.Find the factorial of a number taken as input using while loop
"""
try:
    num=int(input("enter to print factorial :"))
    if(num<0):
        print("Enter postive number")
    else:
        fact=1
        i=1
        while i < num+1:
            fact=fact*i
            i +=1 
    print("the factorial of" ,num ,"is",fact)

except ValueError:
    print("Invalid input !")