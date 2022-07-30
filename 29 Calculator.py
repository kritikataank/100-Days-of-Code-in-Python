def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    want_to_continue = True
    while want_to_continue:
        operator_symbol = input("Pick an operator: ")
        num2 = float(input("What's  the next number? "))
        Calculation_function = operations[operator_symbol]
        first_answer = Calculation_function(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {first_answer}")

        ans = input(f"Type 'Y' to continue calculating with {first_answer}, or 'N' to exit, or 'S' to start with new values: ")

        if ans  == "Y":
            num1 = first_answer
        elif ans == "N":
            want_to_continue = False
        elif ans == "S":
            calculator()
            want_to_continue = False

calculator()