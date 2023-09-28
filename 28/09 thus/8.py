# Write a list comprehension statement to generate a list of all pairs of odd positive integer values less than 10 where the first value is less than the second value.


pairs = [(x, y) for x in range(1, 10, 2) for y in range(x + 2, 10, 2)]

print("Pairs of odd positive integers less than 10 where the first value is less than the second value:")
print(pairs)
