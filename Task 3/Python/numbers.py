# Step 1: Ask the user to enter three different integers
num1 = int(input("Please enter the first integer: "))
num2 = int(input("Please enter the second integer: "))
num3 = int(input("Please enter the third integer: "))

# Step 2: Calculate the sum of all three numbers
sum_of_numbers = num1 + num2 + num3
print("The sum of all the numbers is:", sum_of_numbers)

# Step 3: Calculate the first number minus the second number
difference = num1 - num2
print("The first number minus the second number is:", difference)

# Step 4: Calculate the third number multiplied by the first number
product = num3 * num1
print("The third number multiplied by the first number is:", product)

# Step 5: Calculate the sum of all three numbers divided by the third number
if num3 != 0:  # To prevent division by zero
    division_result = sum_of_numbers / num3
    print("The sum of all three numbers divided by the third number is:", division_result)
else:
    print("Error: Division by zero is not allowed.")
