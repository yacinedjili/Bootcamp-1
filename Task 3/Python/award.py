# Step 1: Ask the user for the times taken in each event
swimming_time = float(input("Enter the swimming time in minutes: "))
cycling_time = float(input("Enter the cycling time in minutes: "))
running_time = float(input("Enter the running time in minutes: "))

# Step 2: Calculate the total time taken to complete the triathlon
total_time = swimming_time + cycling_time + running_time

# Step 3: Display the total time
print("Total time taken to complete the triathlon:", total_time, "minutes")

# Step 4: Determine the award based on the total time
if total_time <= 100:
    award = "Honorary colours"
elif 101 <= total_time <= 105:
    award = "Honorary half colours"
elif 106 <= total_time <= 110:
    award = "Honorary scroll"
else:
    award = "No award"

# Step 5: Display the award
print("The award received:", award)
