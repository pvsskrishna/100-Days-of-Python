from Programes.Days.Day_10_Project_Calculator.Calculator_art import calculator_image
print(calculator_image)

def add(n1,n2):
    """Adding two numbers"""
    return n1 + n2

def subtract(n1,n2):
    """Subtracting two numbers"""
    return n1 - n2

def multiply(n1,n2):
    """Multiplying two numbers"""
    return n1 * n2

def divide(n1, n2):
    """Dividing two numbers"""
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    start = True
    num1 = int(input("Enter number num1: "))
    while start:

        for symbol in operations:
            print(symbol)
        operator = input("Pick the operator: ")
        num2 = int(input("Enter number num2: "))

        solution = operations[operator](num1,num2)
        output = solution
        print(f"{num1} {operator} {num2} = {output}")


        resume = input(f"type 'y' to continue with {output}, or 'n' to start new cal: ").lower()
        if resume == "y":
            num1 = output
        else:
            start = False
            calculator()

calculator()


