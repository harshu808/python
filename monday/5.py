# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

def acpt(num):
    for i in num:
        if i % 2 == 0:
            print(f"{i} is even number.")
        else:
            print(f"{i} is odd number.")


num = [2, 4, 5, 6, 7, 8]
acpt(num)
