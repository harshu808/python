# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

def two_int(n1, n2):
    if n1 == n2 or n1+n2 == 5 or n1-n2 == 5:
        return True


print(two_int(3, 5))
