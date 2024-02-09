"""
Q5.Python program to check the score from a student ,print grades as A+ if score >= 90,A if 80 or above, B+ if 70 or above and so on... 
     print failed if the score is below 50, if score > 100 print invalid
"""
try:
    score = float(input("Enter the student's score: "))

    if score < 0 or score > 100:
        print("Invalid input ! Please enter a score between 0 and 100.")
    elif score >= 90:
        print("Grade: A+")
    elif score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B+")
    elif score >= 60:
        print("Grade: B")
    elif score >= 50:
        print("Grade: C")
    else:
        print("Failed")
except ValueError:
    print("Invalid input")