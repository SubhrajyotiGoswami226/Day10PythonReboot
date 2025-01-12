def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

calc = True
while calc:
    # Taking user input
    userChoice1 = input("Enter first number: \n")
    userChoice2 = input("Enter second number: \n")
    userChoiceOp = input("Enter the operator: '+' '-' '/' '*'\n")
    
    # Check if the inputs are numbers
    if not (userChoice1.replace('.', '', 1).isdigit() and userChoice2.replace('.', '', 1).isdigit()):
        print("Invalid input. Please enter valid numbers.")
        continue

    # Convert inputs to float
    userChoice1 = float(userChoice1)
    userChoice2 = float(userChoice2)

    # Perform operations based on the operator
    if userChoiceOp == '+':
        print(f"The result is: {add(userChoice1, userChoice2)}")
    elif userChoiceOp == '-':
        print(f"The result is: {sub(userChoice1, userChoice2)}")
    elif userChoiceOp == '*':
        print(f"The result is: {mult(userChoice1, userChoice2)}")
    elif userChoiceOp == '/':
        if userChoice2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"The result is: {div(userChoice1, userChoice2)}")
    else:
        print("Invalid operator. Please use one of: '+', '-', '*', '/'.")

    # Asking if the user wants to continue
    continueCalc = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if continueCalc != 'yes':
        calc = False
        print("Calculator exiting. Goodbye!")
