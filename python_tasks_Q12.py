"""
Q12.Print first 10 fibonacci numbers using 'for' and 'while' loops
"""
fibonacci_series = [0, 1]

# Using 'for' loop
for i in range(2, 10):
    next_fibonacci = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(next_fibonacci)

print("First 10 Fibonacci numbers using 'for' loop:")
for num in fibonacci_series:
    print(num, end=" ")

fibonacci_serie = [0, 1]

# Using 'while' loop
i = 2
while i < 10:
    next_fibonacci = fibonacci_serie[-1] + fibonacci_serie[-2]
    fibonacci_serie.append(next_fibonacci)
    i += 1

print("\nFirst 10 Fibonacci numbers using 'while' loop:")
for num in fibonacci_serie:
    print(num, end=" ")




