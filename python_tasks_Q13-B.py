"""
Q13   print the following patterns
(b)
	o
	1 2
	3 4 5
	6 7 8 9
"""
sum=0
for i in range(0, 4):
    
    for k in range(0, i + 1):
        print(sum ,end=" ")
        sum+=1

    
    print()