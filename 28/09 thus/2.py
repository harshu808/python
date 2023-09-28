# Use map and a lambda function to convert a list of Fahrenheit temperatures to a list of Celsius temperatures.
#Celsius = (Fahrenheit - 32) * 5/9

temp = [32, 45, 67, 87]
map1 = list(map(lambda x: (x-32)*5/9, temp))
print(map1)
