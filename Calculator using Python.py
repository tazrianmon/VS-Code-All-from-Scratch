# Simple Calculator (Project 1)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is undefined.")
    return a / b

def modulus(a, b):
    if b == 0:
        raise ValueError("Modulus by zero is undefined.")
    return a % b

def get_number(prompt):
    """Safely read a number from user input as float."""
    while True:
        text = input(prompt).strip()
        try:
            return float(text)
        except ValueError:
            print("Invalid input: please enter a numeric value (e.g., 7, 3.5, -0.2).")

def get_choice():
    """Prompt until a valid operation choice is selected."""
    menu = (
        "Select operation:\n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n"
        "5. Modulus"
    )
    print(menu)
    while True:
        choice = input("Enter choice (1/2/3/4/5): ").strip()
        if choice in {"1", "2", "3", "4", "5"}:
            return choice
        print("Invalid choice: please enter 1, 2, 3, 4, or 5.")

def main():
    choice = get_choice()
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    operations = {
        "1": (add, "+"),
        "2": (subtract, "-"),
        "3": (multiply, "*"),
        "4": (divide, "/"),
        "5": (modulus, "%"),
    }

    func, symbol = operations[choice]

    try:
        result = func(a, b)
        # Format: division shows two decimals like 2.50; others show default float form
        if choice == "4":
            formatted_result = f"{result:.2f}"
        else:
            formatted_result = f"{result}"
        print(f"{a} {symbol} {b} = {formatted_result}")
    except ValueError as e:
        # Handles division/modulus by zero or any other ValueError raised
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
