"""
  Write python programs , which accept two inputs and perform the following arithmetic operations
	i)    Addition (+)
    ii)   Subtraction (-)
    iii)  Multiplication (*)
    iv)   Division (/)
    v)    Modulus (%)
    vi)   Exponentiation (**)
    vii)  Floor Division (//)  
"""

# Store input numbers
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
# Division
def division(x, y):
    
    if y == 0:
        return "Division by zero is not allowed"
    result = x / y
    return result
# Modulus
def Modulus(x, y):
    
    if y == 0:
        return "Division by zero is not allowed"
    result = x % y
    return result
# Floor Division
def floor_division(x, y):
    if y == 0:
        return "Floor division by zero is not allowed"
    result = x // y
    return result


print("Addition ",num1,"+" ,num2 , "=", num1+num2)
print("Subtraction ",num1,"-" ,num2 , "=", num1-num2)
print("Multiplication ",num1,"*" ,num2 , "=", num1*num2)
print("Division",num1,"/" ,num2 , "=",division(num1, num2))
print("Modulus",num1,"%" ,num2 , "=", Modulus(num1, num2))
print("Exponentiation", num1, "power", num2,  "=", num1 ** num2)
print("Floor Division",num1,"//" ,num2 , "=", Modulus(num1, num2))




