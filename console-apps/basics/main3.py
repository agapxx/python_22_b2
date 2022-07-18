# Python Functions / Methods
def validateInput(strInput="file.exe"):
    if "." not in strInput:
        response = "The file name is invalid. '.' is missing"
    else:
        response = strInput
    return response

def calculate(num1=0, num2=0, operation="a"):
    if operation == "a":
        result = num1 + num2
    elif operation == "d":
        result = float(num1 / num2)
    elif operation == "m":
        result = num1 * num2
    elif operation == "s":
        result = num1 - num2

    return result

def calculator(choice):
    if choice == "1":
        num1 = int(input("Please enter first operand"))
        num2 = int(input("Please enter second operand"))
        retvalue = calculate(num1,num2,"a")
    elif choice == "2":
        num1 = int(input("Please enter first operand"))
        num2 = int(input("Please enter second operand"))
        retvalue = calculate(num1, num2, "d")
    elif choice == "3":
        num1 = int(input("Please enter first operand"))
        num2 = int(input("Please enter second operand"))
        retvalue = calculate(num1, num2, "m")
    elif choice == "4":
        num1 = int(input("Please enter first operand"))
        num2 = int(input("Please enter second operand"))
        retvalue = calculate(num1, num2, "s")
    else:
        retvalue = "Wrong input encountered. Please enter 1 or 2 or 3 or 4"

    return retvalue


# userInput = input("Enter a valid file name")
# if userInput != "":
#     returned = validateInput(userInput)
#     print(returned)

print("My simple calculator. Select an operation below to continue")
choice = (input("1. Addition \n2. Division \n3. Multiplication \n4. Subtraction \n\nEnter choice:\t"))
print(calculator(choice))

if choice == "1":
    num1 = int(input("Please enter first operand"))
    num2 = int(input("Please enter second operand"))
    sum = num1 + num2
    print(f"The addition of {num1},and {num2} is :\t{sum}")
elif choice == "2":
    num1 = int(input("Please enter first operand"))
    num2 = int(input("Please enter second operand"))
    div = float(num1 / num2)
    print(f"The division of {num1},and {num2} is :\t{div}")
elif choice == "3":
    num1 = int(input("Please enter first operand"))
    num2 = int(input("Please enter second operand"))
    mul = num1 * num2
    print(f"The subtraction of {num1},and {num2} is :\t{mul}")
elif choice == "4":
    num1 = int(input("Please enter first operand"))
    num2 = int(input("Please enter second operand"))
    sub = num1 - num2
    print(f"The subtraction of {num1},and {num2} is :\t{sub}")
else:
    print("Wrong input encountered. Please enter 1 or 2 or 3 or 4")
