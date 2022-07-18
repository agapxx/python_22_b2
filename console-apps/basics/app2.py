#Write a program
#- that targets 3 file names from a user with the filenames having >= 15char
#- print the estension and

# #solution
file1 = file2 = file3 =""
print("Welcome User,Kindly enter 3 filenames (minimum of 15 chars) and I will print out the extensions as well as the char-count")

l1 = "true"
while(l1 == 'true'):
    file1 = input("Enter the first filename")
    if len(file1) >= 15:
        l1 = 'false'
    else:
        print("The filename is less than 15 characters")

l2 = "true"
while(l2 == 'true'):
    file2 = input("Enter the second filename")
    if len(file1) >= 15:
        l2 = 'false'
    else:
        print("The filename is less than 15 characters")


l3 = "true"
while(l3 == 'true'):
    file3 = input("Enter the third filename")
    if len(file1) >= 15:
        l3 = 'false'
    else:
        print("The filename is less than 15 characters")

print("Thanks for the input, Kindly find my output below as I've promised")
# print("File 1 extension:'{}' | File 1 char-count: {} | Ext char-count {}".format(file1[-4]) len(file1), len(file1[-4:])) ")
print(f"\nFile 1 extension: '{file2[-4:]}' | File 1 char-count: {len(file1)} | Ext char-count {len(file1[-4:])}")
print(f"\nFile 2 extension: '{file2[-4:]}' | File 2 char-count: {len(file2)} | Ext char-count {len(file2[-4:])}")
print(f"\nFile 3 extension: '{file3[-4:]}' | File 3 char-count: {len(file3)} | Ext char-count {len(file3[-4:])}")





