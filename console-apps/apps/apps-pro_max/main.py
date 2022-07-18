stdFNames = []
stdLNames = []
stdEmails = []
stdPwds = []
stdCourses = []
courseFees = []

def getValue(msg,listvar,):
    lk = True
    while lk == True:
        val = input(f"Enter {msg}")
        if val != "":
            print(f"{msg} added successfully")
            listvar.append(val)
            lk = False
        else:
            print(f"{msg} cannot be empty")

def getEmail():
    lk = True
    while lk == True:
        val = input(f"Enter Email")
        if val != "":
            if val not in stdEmails:
                stdEmails.append(val)
                print(f"email added successfully")
                lk = False
            else:
                print("email already exists. Try again")
        else:
            print(f"email cannot be empty")

def fetchStdDetails():
    lk = 0
    while lk < len(stdFNames):
        print(f"First Name: {stdFNames[lk]} | Last Name: {stdLNames[lk]} | Email: {stdEmails[lk]}")
        lk += 1

def validateEmail(email):
    if len(stdEmails) == 0:
        stdIndex = "null"
    else:
        lk = 0
        while lk < len(stdEmails):
            if stdEmails[lk] == email:
                stdIndex = lk
            else:
                stdIndex = False
        return stdIndex

def confirmUpdate(item, list):
    cUpd = input(f"would you like to update the {item}? y/n")
    if cUpd == "y" or cUpd == "Y":
        val = input("enter the new value")
        lk = True
        while lk == True:
            if val == "":
                print("you must enter a value. Try again")
            else:
                list[index] = val
                print(f"{item} updated successfully")
                lk = False
    elif cUpd == "n" or cUpd == "N":
        pass


while True:
    print("-------------------- AFRIHUB Institute --------------")
    print("H1, what would you like today?")
    print("1. Add Student \n2. View Students \n3. Update Student \n4. Update Fee \n5. Remove Student \n6. Quit")
    userChoice = input("Please enter your choice")

    if userChoice == "1":
        getValue("first name", stdFNames)
        getValue("last name", stdLNames)
        getValue("email", stdEmails)
        getValue("password", stdPwds)
        getValue("course", stdCourses)
        getValue("fee", courseFees)

        fetchStdDetails()

    elif userChoice == "2":
        fetchStdDetails()

    elif userChoice == "3":
        stdEmail = input("enter student email to continue")
        chkEmail = validateEmail(stdEmail)
        if chkEmail != False:
            index = chkEmail
        elif chkEmail == "null":
            print("no student has been registered")
        else:
            print("invalid email supplied")

        confirmUpdate("first name",stdFNames)
        confirmUpdate("last name",stdLNames)
        confirmUpdate("password",stdPwds)



    elif userChoice == "4":
        pass
    elif userChoice == "5":
        pass
    elif userChoice == "6":
        print("See you later")
        exit()
    else:
        print("You entered a wrong input, Try again")
        restart = input("Please press enter key to restart")