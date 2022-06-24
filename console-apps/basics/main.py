# print("welcome to my App")
# print("*****************")
#
# fName = input("Enter your first name\t")
# lName = input("Enter your last name\t")
# age = input("How old are you\t")
#
# print("\n\nThanks for your response, Kindly find the summary below\n\n")
# print(f"Your name is {fName} {lName} and you are {age}yrs old")

# pascal casing MyFirstName
# camel casing  myFirstName
# snake casing  my_first_name
# normal casing myfirstname

#python strings
name = "agapxx machiavelli"
bio = """fjbzdfkjb
sdkvbzvj guru software engineer
dvfbzjkb
"""

print(name[5]+"\n"+bio[20])

# for letter in name:
#     print(letter)

# getting string length len(str)
print(f"My names contains {len(name)} letters")
print(f"My bio contains {len(bio)} letters")

#checking for a value in string "in | val not in"
print("hannah" not in name)

# slicing string "[i:i]"
subName = name[-5:]
# print(subName)
if subName == '.png':
    print("Well Job")
else:
    print("Bad Job")

#string modification e.g casing, replacing, split etc.
print(name.upper())
# print(name.lower())
# print(name.capitalize())

print(name.replace("agapxx", "Nisan Dave"))

print(name.format(" "))


