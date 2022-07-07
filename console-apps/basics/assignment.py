print('************   Welcome to my Newsletter app ************\n How may i help you? \n')
n1 = 'True'
while n1 == 'True':
    print('Select:\n 1. View email address\n 2. Add email address\n')
    userPreference = int(input('Enter 1 to view email address or 2 to add email address\t'))
    existingMails = ['love@gmail.com','mrT@yahoo.com']
    n2 ='True'
    while n2 == 'True':
        if userPreference == 1:
            n2 = 'False'
            print(existingMails)
            emailLength = len(existingMails)
            if emailLength > 1:
                print(f'There are {len(existingMails)} emails on the list')
            elif emailLength <= 1:
                print(f'There is {len(existingMails)} email on the list')
            break
        elif userPreference == 2:
            addedMail = input('Enter the mail address you want added to the list')
            existingMails.append(addedMail)
            print(existingMails)
            emailLength2 = len(addedMail)
            if emailLength > 1:
                print(f'There are {len(existingMails)} email address on the list')
            elif emailLength <= 1:
                print(f'There is {len(existingMails)} email address on the list')
        else:
            print('please enter a valid input')
        userEntry = input('still want to add more email addresses? y or n:\t')
        if userEntry == 'y' or userEntry == 'Y':
            n2 = 'True'
        elif userEntry == 'n' or userEntry =='N':
            n2 = 'False'
        else:
            print('Baba enter valid input abeg!')

    userActivity = input('press c to continue or q to end function')
    if userActivity == 'c' or userActivity == 'C':
        n1 = 'True'
    if userActivity == 'q' or userActivity == 'Q':
        n1 = 'False'
        print('Thanks for the patronage')
    else:
        print('please enter a valid input')