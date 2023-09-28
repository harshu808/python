# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)

digit = [num for num in range(1, 1001) if any(
    num % divisor == 0 for divisor in range(2, 10))]
print(digit)
