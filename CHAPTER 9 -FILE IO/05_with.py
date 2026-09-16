f = open("CHAPTER 9 -FILE IO/file.txt")
data = f.read()
print(data)
f.close()


# same -> with statement : 
with open("CHAPTER 9 -FILE IO/file.txt") as f:
    print(f.read())

#do not need to close the file. 