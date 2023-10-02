'''2.get one num as input find out sum of digts of numbers using for and while loop?'''
# Take an input number from the user
num = input("Enter a number: ")

# Initialize a variable to store the sum of digits
sum_of_digits = 0

'''# Use a while loop to extract digits and calculate the sum
while num > 0:
    # Extract the last digit using the modulo operator
    digit = num % 10
    
    # Add the extracted digit to the sum
    sum_of_digits += digit
    
    # Remove the last digit from the number
    num //= 10

# Print the sum of digits
print("Sum of digits:", sum_of_digits)'''

# Iterate through each character (digit) in the string
for digit in num:
    # Convert the character back to an integer and add it to the sum
    sum_of_digits += int(digit)

# Print the result
print("Sum of digits:", sum_of_digits)
