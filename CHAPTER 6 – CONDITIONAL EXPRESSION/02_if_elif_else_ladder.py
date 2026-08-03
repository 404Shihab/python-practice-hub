year = int(input("Enter your Birth year: "))

if year < 1900 or year >= 2026:
    print("You are entering wrong year")
elif (2026 - year) >= 18:
    age = 2026 - year
    print("You are ", age, " years old")
    print("You are eligible to vote")
else:
    age = 2026 - year
    print("You are ", age, " years old")
    print("You are not eligible to vote")