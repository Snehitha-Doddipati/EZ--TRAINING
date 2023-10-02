'''2. create a dynamic  array it should contain btw 20 t0 30 Extract and print an even number and 2 power values?'''
import random

# Generate a dynamic array with random values between 20 and 30 (inclusive)
array_length = random.randint(20, 30)
dynamic_array = [random.randint(20, 30) for _ in range(array_length)]

print("Dynamic Array:", dynamic_array)

# Extract and print even numbers
even_numbers = [num for num in dynamic_array if num % 2 == 0]
print("Even Numbers:", even_numbers)

# Calculate and print 2^power values for each element
power_values = [2 ** num for num in dynamic_array]
print("2^Power Values:", power_values)

