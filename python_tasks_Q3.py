"""
Q3 Print the greatest of the 3 numbers taken as input, print equal if all three numbers are the same

"""
num1=float(input("enter the  first number :"))
num2=float(input("enter the  Second number : "))
num3=float(input("enter the  Third number :"))

if(num1==num2==num3):
    print("all three numbers are the same")
elif(num1>num2):
    if(num1>num3):
       print("the greatest of the 3 numbers :",num1)
    else:
        print("the greatest of the 3 numbers :",num3)
elif(num1<num2):
    if(num2>num3):
       print("the greatest of the 3 numbers :",num2)
    else:
        print("the greatest of the 3 numbers :",num3)
