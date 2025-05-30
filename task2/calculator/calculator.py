def calculate(a, b, operator):
    try:
        a, b = float(a), float(b)
        if operator == '+': return a + b
        elif operator == '-': return a - b
        elif operator == '*': return a * b
        elif operator == '/': return a / b
        else: raise ValueError("Unsupported operator")
    except ZeroDivisionError:
        return "Error: Division by zero"
    except ValueError as ve:
        return f"Error: {ve}"

def main():
    print("🧮 Simple Calculator")
    while True:
        a = input("Enter first number (or 'q' to quit): ")
        if a.lower() == 'q': break
        b = input("Enter second number: ")
        op = input("Enter operator (+ - * /): ")
        result = calculate(a, b, op)
        print("Result:", result)

if __name__ == "__main__":
    main()
