import os



# FILE HANDLING
file = open("sample.txt", "r")

print(file.read())


myTxt =open("C:\\Users\\Agape love\\Document s\\python-notes.txt", "r")

# print(myTxt.read(100))
print(myTxt.readline())
print(myTxt.readline())
print(myTxt.readline())
print(myTxt.readline())

file.close()

file = open("sample.txt", "a")
file.write("\nI will be appended to the end of the file")
file.close()
file = open("sample.txt", "r")
print(file.read())
file.close()

if os.path.exists("sample.txt"):
    os.remove("sample.txt")
else:
    print("No such file encountered")




