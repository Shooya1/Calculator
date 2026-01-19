def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

operations = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide
}

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option: ")
    
    if choice == "5":
        print("Goodbye")
        break

    if choice not in operations:
        print("Invalid choice.")
        continue

    try:
        a = float(input("Enter first operand: "))
        b = float(input("Enter second operand: "))
    except ValueError:
        print("Invalid input.")
        continue
   

    result = operations[choice](a, b)
    print(f"Result: {result}")
