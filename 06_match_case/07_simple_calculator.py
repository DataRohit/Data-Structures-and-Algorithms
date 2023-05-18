# User input for number and operator
num1 = int(input())
op = input()
num2 = int(input())


# Match case to check for operator
match op:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case "//":
        print(num1 // num2)
    case "%":
        print(num1 % num2)
    case "**":
        print(num1**num2)
    case _:
        print("invalid")
