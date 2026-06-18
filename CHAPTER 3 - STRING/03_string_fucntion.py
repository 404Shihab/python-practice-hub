name = "Shihab Uddin Bhuiyan "

# Returns the total number of characters in the string
print(len(name))  # 21

# Checks if the string ends with the given value
print(name.endswith(" "))  # True

# Counts how many times a character or substring appears
print(name.count("n"))  # 2

# Capitalizes the first character and makes the rest lowercase
print(name.capitalize())  # Shihab uddin bhuiyan

# Finds the first occurrence of a substring and returns its index
print(name.find("dd"))  # 8

# Replaces a substring with another substring
print(name.replace("Uddin", "Bin"))  # Shihab Bin Bhuiyan

# Converts all characters to uppercase
print(name.upper())  # SHIHAB UDDIN BHUIYAN

# Converts all characters to lowercase
print(name.lower())  # shihab uddin bhuiyan

# Removes leading and trailing whitespace
print(name.strip())  # Shihab Uddin Bhuiyan

# Checks if the string starts with the given value
print(name.startswith("Shi"))  # True

# Checks if all characters are alphabetic
print("Shihab".isalpha())  # True

# Checks if all characters are digits
print("12345".isdigit())  # True

# Converts the first letter of each word to uppercase
print(name.title())  # Shihab Uddin Bhuiyan

# Swaps uppercase to lowercase and vice versa
print("Shihab".swapcase())  # sHIHAB