# Find all of the numbers from 1–1000 that have a 6 in them
num = 6
six = [print(i) for i in range(1, 1001) if str(num) in str(i)]
