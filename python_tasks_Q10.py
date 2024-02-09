"""
Q10.Find the sum of all even numbers between the range given by user
"""
try:
    lower_limit=int(input("Enter the lower limit :"))
    upper_limit=int(input("Enter the upper limit :"))
    sum=0
    for i in range(lower_limit,upper_limit+1):
    
        if(i%2==0):
            sum+=i
            

    
    print(f"the sum of all even numbers between {lower_limit} to {upper_limit} is : {sum}")

except ValueError:
    print("Invalid input !")