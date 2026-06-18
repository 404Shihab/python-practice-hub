# Write a python program to display a user entered name followed by Good Afternoon using input() function.

name = input("Enter your name: ")
print (f"Good Afternoon {name}. How are you ?")  #f-string

# Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "java khan").replace("<|Date|>", "18 june, 2026"))


# Write a program to detect double space in a string.

string = input("Enter a string : ")
print(string.find("  "))


#Replace the double space from problem 3 with single spaces.
name = "Shihab Uddin  Bhuiyan"
print(name.replace("  "," "))
print(name) #Shihab Uddin  Bhuiyan --->> strings are immutable , which means that cannot change them by running function on them