# Step 1: Initialize sum and count variables
total_sum = 0
count = 0

# Step 2: Use a while loop to ask the user to enter numbers continuously
while True:
    user_input = int(input("Enter a number (enter -1 to stop): "))
    
    # Step 3: Break the loop if the user enters -1
    if user_input == -1:
        break
    
    # Step 4: Ignore 0 as it is not a valid input
    if user_input == 0:
        continue
    
    # Step 5: Add valid input to total_sum and increase the count
    total_sum += user_input
    count += 1

# Step 6: Check if any valid numbers were entered
if count > 0:
    # Step 7: Calculate and display the average
    average = total_sum / count
    print("The average of the valid numbers is:", average)
else:
    print("No valid numbers were entered.")
