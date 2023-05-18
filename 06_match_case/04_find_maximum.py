# User input for num1 and num2
num1, num2 = map(int, input().split())


# Match case to check for greater number
match num1 > num2:
    case True:
        print(num1)
    case False:
        print(num2)
