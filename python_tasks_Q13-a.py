"""
Q13   print the following patterns
(a)
	    *
       * *
      * * *
     * * * *
"""

for i in range(1, 5):
    for j in range(5, i-1,-1):
        print(end=" ")
    for k in range(1, i + 1):
        print("*" ,end=" ")

    
    print()
