def a_input():
    while True:
        try:
            return float(input("Insert first number: "))
        except ValueError:
            print("Not a number, try again")
def b_input():
    while True:
        try:
            return float(input("Insert second number: "))
        except ValueError:
            print("Not a number, try again")
def operation():
    while True:
        op = input("Choose operation (+, -, *, /, ^): ")
        if op in ["+", "-", "*", "/", "^"]:
            return op
        else:
            print("Invalid operator, try again")
def multiply(a, b):
    print(a * b)
def power_of(a, b):
    result = 1
    for _ in range(int(b)):
        result *= a
    print (result)
def divide(a, b):   
    while True:
            if b == 0:
                print("cant divide by zero, try again")
                b = b_input()
            elif b != 0: 
                print(a / b)
                break
def add(a, b):
    print(a + b)
def min (a, b):
    print(a - b)

a = a_input()
o = operation()
b = b_input()

match o:
    case "^":
        power_of(a, b)
    case "*":
        multiply(a, b)
    case "/":
        divide(a, b)
    case "+":
        add(a, b)
    case "-":
        min(a, b)
    
        
    


    