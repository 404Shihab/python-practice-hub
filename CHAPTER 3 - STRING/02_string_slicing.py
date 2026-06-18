text = "Python"

print(text[0:3])   # Pyt  (index 0 to 2)

# Omitting start index
print(text[:4])    # Pyth (starts from index 0)

# Omitting end index
print(text[2:])    # thon (goes until the last index)

# Omitting both start and end
print(text[:])     # Python (entire string)

# Negative indexing
print(text[-1])    # n (last character)

# Step slicing
print(text[::2])   # Pto (every 2nd character)

# Reverse string
print(text[::-1])  # nohtyP