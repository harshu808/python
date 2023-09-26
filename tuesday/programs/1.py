# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

def num(n1, n2, n3):
    if n1 == n2 or n2 == n3 or n1 == n3:
        sum1 = 0
    else:
        sum1 = (n1+n2+n3)
    return sum1


print(num(1, 2, 3))
print(num(3, 4, 5))
