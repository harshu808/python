# Write a Python program to add two objects if both objects are integers.

def num(n1, n2):
    if type(n1) == int and type(n2) == int:
        sum1 = n1+n2
        return sum1


print(num('20', 30))
