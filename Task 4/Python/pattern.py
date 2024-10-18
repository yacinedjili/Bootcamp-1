# Step 1: Use a single for loop to print the arrow pattern
for i in range(1, 10):
    if i <= 5:
        # Step 2: Print increasing number of asterisks when i is less than or equal to 5
        print('*' * i)
    else:
        # Step 3: Print decreasing number of asterisks when i is greater than 5
        print('*' * (10 - i))
