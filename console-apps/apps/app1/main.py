# import os, platform
import os, platform
global stdList
stdList = ['Agapxx', 'John Wick', 'Playboi Carti']

def runApp():
    x = '#' * 30
    y = '=' * 30
    global exitMsg
    exitMsg = f'\n{x} \n{y} \n==> Built by <==\n==> AGAPXX <== \n{y}\n{x}'
    print("""
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    |============================================|
    |======= Welcome User, How can we help ======|
    |============================================|
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Enter 1: To View all Students
    Enter 2: To Add new Students
    Enter 3: To Remove all Students
    Enter 4: To Find all Student(s)
    """)

    try:
        userInput = int(input('Please enter an option'))
    except ValueError:
        exit('Dondore. You are supposed to type a number')
    else:
        print('\n')

    if(userInput == 1):  #View
        print('Student list\n')
        for std in stdList:
            print(f'=> {std}')

    elif(userInput == 2):
        newStd = input('Enter student name')
        if newStd in stdList:
            print(f'Student with name {newStd} exists')
        else:
            stdList.append(newStd)
            print(f'\nStudent {newStd} added successfully as shown in the list below')
            for std in stdList:
                print(f'=> {std}')

    elif userInput == 3: #remove
        stdName = input('Enter the student name')
        if(stdName in stdList):
            stdList.remove(stdName)
            print(f'=> Student {stdName} removed successfully')
            for std in stdList:
                print(f'=> {std}')
        else:
            print(f'Student {stdName} not found')

    elif userInput == 4: #find
        stdName = input('Enter the student name')
        if stdName in stdList:
            print(f'Student {stdName} exists')
        else:
            print(f'Student {stdName} not found')

    elif(userInput < 1 or userInput > 4):
        print('Invalid option Idiot')

runApp()

def restartApp():
    restart = input('Restart App? y/n')
    if restart.lower() == 'y':
        if platform.system() == 'Windows':
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        runApp()
        restartApp()
    else:
        #used to quit
        quit(exitMsg)

restartApp()