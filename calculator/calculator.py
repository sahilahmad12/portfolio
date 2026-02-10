from calculator.operations import add, subtract, multiply, divide

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate(a, operator, b):
    if operator not in OPERATIONS:
        raise ValueError("Invalid operator")

    return OPERATIONS[operator](a, b)
