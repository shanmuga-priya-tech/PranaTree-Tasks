num1 = float(input("Enter Number1 to Calculate: "))
num2 = float(input("Enter Number2 to Calculate: "))
operand = input("Enter the operation: ")

def calculator(num1,num2,operand):
    if operand == "+":
        return num1 + num2
    elif operand == "-":
        return num1 - num2
    elif operand == "*":
        return num1 * num2
    elif operand == "/":
        return num1 / num2
    else:
        print("Invalid operation. Operations allowed ( + , - , * , /)")

print(calculator(num1,num2,operand))