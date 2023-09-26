# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

def sum_of(n1, n2):

    ans = n1 + n2
    if 15 < ans < 20:
        return 20


print(sum_of(10, 9))
