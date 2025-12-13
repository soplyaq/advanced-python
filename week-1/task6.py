
num1 = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
num2 = float(input("Second number: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print(num1 / num2)
else:
    print("Invalid operation")