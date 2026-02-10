import csv
from calculator.calculator import calculate


def log_operation(a, operator, b, result):
    with open("logs/operations.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([a, operator, b, result])


def main():
    print("CLI Calculator")
    print("Operations: +  -  *  /")

    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        b = float(input("Enter second number: "))

        result = calculate(a, operator, b)
        print(f"Result: {result}")

        log_operation(a, operator, b, result)

    except ValueError:
        print("Invalid input or operator.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


if __name__ == "__main__":
    main()
