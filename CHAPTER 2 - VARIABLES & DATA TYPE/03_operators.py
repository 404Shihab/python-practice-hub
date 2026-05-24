# 1. Arithmetic operators: +, -, *, / etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc.
# 4. Logical operators: and, or, not.



# 1. Arithmetic Operators
a = 10
b = 3

print("a =", a, "b =", b)
print("Addition (+):", a + b)
print("Subtraction (-):", a - b) 
print("Multiplication (*):", a * b)
print("Division (/):", a / b) 
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b) 
print("Exponent (**):", a ** b) 

# 2. Assignment Operators

x = 5
print("Initial x =", x)

x += 3   # x = x + 3
print("x += 3 ->", x)

x -= 2   # x = x - 2
print("x -= 2 ->", x)

x *= 4   # x = x * 4
print("x *= 4 ->", x)

x /= 2   # x = x / 2
print("x /= 2 ->", x)


# 3. Comparison Operators

p = 10
q = 20

print("p =", p, "q =", q)
print("p == q:", p == q)   
print("p != q:", p != q)  
print("p > q :", p > q)    
print("p < q :", p < q)   
print("p >= q:", p >= q)   
print("p <= q:", p <= q)  


# 4. Logical Operators

age = 18
has_nid = True

print("age =", age, "has_nid =", has_nid)

# and: both conditions must be True
print("Eligible (age >= 18 and has_nid):", age >= 18 and has_nid)

# or: at least one condition True
print("Special case (age < 18 or has_nid):", age < 18 or has_nid)

# not: reverse the condition
print("Not eligible:", not (age >= 18))
