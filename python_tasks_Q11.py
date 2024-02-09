"""
Q11.Find the sum of all odd numbers between the range given by user using while loop
"""
try:
    lower_limit=int(input("Enter the lower limit :"))
    upper_limit=int(input("Enter the upper limit :"))
    sum=0
    i=1
    while(i<upper_limit+1):
    
    
        if(i%2!=0):
            sum+=i
        i+=1
            

    
    print(f"the sum of all odd numbers between {lower_limit} to {upper_limit} is : {sum}")

except ValueError:
    print("Invalid input !")