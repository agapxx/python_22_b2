"""
Search and replace console app
"""
while(True):
    print("############# Search & Replace ############")
    userStr = input("please enter your desired string to continue:\n")

    userChoice = input("Would you like to replace anything in your string? y/n")

    if userChoice == 'y':
        oldStr  = input("Please provide the string to be replaced\t")
        newStr  = input("Please provide the new string")
        newUserStr = userStr.replace(oldStr, newStr)
        print("The replacement was done successfully. See the summary below")
        print(f"OLD String: ({len(userStr)} chars):\n {userStr}")
        print(f"NEW String: ({len(newUserStr)} chars):\n {newUserStr}")
    elif userChoice == 'n' or userChoice == 'N':
        print("Kindly find your string below:\n"+userStr)
        print("\n\nThank you for using our app, see you soon")
    else:
        print("you are expected to enter 'y' or 'n'")
    restart = input("Press 'c' or 'q' to terminate or press 'enter' to continue:\n")
    if restart == "c" or restart == "q":
        break

