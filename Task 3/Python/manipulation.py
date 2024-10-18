# Step 1: Ask the user to enter a sentence
str_manip = input("Please enter a sentence: ")

# Step 2: Calculate and display the length of str_manip
length_of_str = len(str_manip)
print("The length of the sentence is:", length_of_str)

# Step 3: Find the last letter of the sentence
last_letter = str_manip[-1]

# Step 4: Replace every occurrence of the last letter with '@' (case-sensitive)
modified_str = str_manip.replace(last_letter, '@')
print("Modified string:", modified_str)

# Step 5: Print the last three characters of str_manip in reverse
last_three_reversed = str_manip[-3:][::-1]
print("The last three characters in reverse are:", last_three_reversed)

# Step 6: Create and print a five-letter word made of the first 3 characters and the last 2 characters
if len(str_manip) >= 5:  # Ensure the input string has at least 5 characters
    five_letter_word = str_manip[:3] + str_manip[-2:]
    print("The new five-letter word is:", five_letter_word)
else:
    print("The sentence is too short to form a five-letter word.")
