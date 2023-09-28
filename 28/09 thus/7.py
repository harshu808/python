# Write a list comprehension statement to convert a list of Fahrenheit temperatures to Celsius

fahrenheit_temperatures = [68, 75, 90, 55, 32, 82, 95, 70]

celsius_temperatures = [(temp - 32) * 5/9 for temp in fahrenheit_temperatures]

print("Fahrenheit Temperatures:", fahrenheit_temperatures)
print("Celsius Temperatures:", celsius_temperatures)
