# Use filter to determine the percentage of Fahrenheit temperatures in a list are within the range 32 to 80

# List of Fahrenheit temperatures
fahrenheit_temperatures = [68, 75, 90, 55, 32, 82, 95, 70]

# Use filter to select temperatures within the range 32 to 80
filtered_temperatures = list(
    filter(lambda temp: 32 <= temp <= 80, fahrenheit_temperatures))

# Calculate the percentage
percentage_within_range = (
    len(filtered_temperatures) / len(fahrenheit_temperatures)) * 100

# Display the result
print("List of Fahrenheit Temperatures:", fahrenheit_temperatures)
print("Temperatures within the range 32 to 80:", filtered_temperatures)
print("Percentage within the range: {:.2f}%".format(percentage_within_range))
