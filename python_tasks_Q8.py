"""
Q8.Find the factorial of a number taken as input using for loop
"""
try:
    num=int(input("enter to print factorial :")) 
    if(num<0):
        print("Enter postive number")
    else:
        fact=1
        for i in range(1,num+1):
            fact=fact*i
    
    print("the factorial of" ,num ,"is",fact)
        

except ValueError:
    print("Invalid input !")