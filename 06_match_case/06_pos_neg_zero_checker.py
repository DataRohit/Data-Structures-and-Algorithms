# User input for number
num = int(input())


# Match case to check and print
match num > 0:
    case 1:
        print("positive")
    case 0:
        match num < 0:
            case 1:
                print("negative")
            case 0:
                print("zero")
