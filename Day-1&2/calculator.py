def calculator(numbers, operand):
    if not numbers:
        return 0

#initialize with first num to perform operation with rest
    result = numbers[0]
    for num in numbers[1:]:
        if operand == "+":
            result += num
        elif operand == "-":
            result -= num
        elif operand == "*":
            result *= num
        elif operand == "/":
            if num == 0:
                return "Error: Division by zero"
            result /= num
        else:
            return "Invalid operation. Use +, -, *, /"
    return result


user_input = input("Enter numbers separated by space: ")
string_list = user_input.split()
float_list = map(float, string_list)
nums = list(float_list)
op = input("Enter the operation (+, -, *, /): ")

print("Result:", calculator(nums, op))
