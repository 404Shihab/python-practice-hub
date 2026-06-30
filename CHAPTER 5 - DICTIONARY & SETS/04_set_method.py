s = {45, 89, 693, 10, 20, 3.99, 78.00, "45", True}

s.add(False)
print(type(s))

print("Length of the set:")
print(len(s))


print("Using remove():")

s.remove(89)
print("After removing 89:")
print(s)
print()

# Uncomment the line below to see KeyError
# s.remove(100)

# pop() -> Removes and returns a random element
# Since sets are unordered, you don't know
# which element will be removed.
# ----------------------------------------
print("Using pop():")

removed_item = s.pop()
print("Removed element:", removed_item)
print("Updated set:")
print(s)

# union() -> Returns a new set containing
# all unique elements from both sets.
# Original set remains unchanged.

print("Using union():")

new_set = s.union({8, 11})

print("New set after union:")
print(new_set)

print("Original set remains:")
print(s)
print()

# ----------------------------------------
# intersection() -> Returns only the common
# elements between two sets.

print("Using intersection():")

common = s.intersection({8, 11, 20, 45})

print("Common elements:")
print(common)
print()

# clear() -> Removes all elements from the set.

print("Using clear():")

s.clear()

print("After clear():")
print(s)