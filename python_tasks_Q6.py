"""
Q6.Python program to print all even/odd numbers in the range given by user
"""


try:
    lower_limit = int(input("Enter the lower limit of the range: "))
    upper_limit = int(input("Enter the upper limit of the range: "))

    if lower_limit > upper_limit:
        print(f"Invalid range. The lower limit {lower_limit} is greater than the upper limit {upper_limit}")
    else:
        print(f"All even numbers in the range {lower_limit} to {upper_limit}:")
        for i in range(lower_limit, upper_limit + 1):
            if i % 2 == 0:
                print(i)

        print(f"All odd numbers in the range {lower_limit} to {upper_limit}:")
        for i in range(lower_limit, upper_limit + 1):
            if i % 2 != 0:
                print(i)

except ValueError:
    print("Invalid input !")






