d ={} # empty  dictionary
marks = {
    "jalil":456,
    "khalil":1023,
    "molil":1023,
    "solil":7492,
    0: "halil", # 0 --  key and "halil" --- value
    "isPass" : True
}

print(marks.items())  # Returns a list of (key,value) tuples

print(marks.keys())  # Returns a list containing dictionary's keys. dict_keys(['jalil', 'khalil', 'molil', 'solil'])

print(marks.values())

marks.update({"jalil":100})

print(marks)

print(marks.get(0))

print(marks.get("jalil2")) # Prints none
print(marks["jalil2"]) # returns an error