def add(n1, n2):
    return n1 + n2


# TODO-1 : Write out the other three functions : subtract,multiple and divide.
def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


# TODO - 2: Add these function into a dictionary as the values . keys = "+","-","*","/"

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


# TODO -3:Use the dictionary to perform the calculations . multiply 4 * 8 using the dictionary
# print(operations["*"](4,8))
def calculator():
    First_number = float(input("Enter the First number : "))
    should_accumulate = True
    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("enter the operation you want : ")
        Second_number = float(input("Enter the second number : "))

        output = operations[operation_symbol](First_number, Second_number)
        print(f"{First_number} {operation_symbol} {Second_number} = {output}")

        choice = input("Type 'y' if you want to continue operations with previous result or 'n' for no : ")

        if choice == "y":
            First_number = output
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()