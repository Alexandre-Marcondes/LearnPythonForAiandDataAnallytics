def main():
    userInput = input("Expression: ")
    interpreter(userInput)


def interpreter(expression):
    x, y, z = expression.split(" ")
    if y == "+":
        sum = float(x) + float(z)
        return print(sum)
    elif y == "-":
        subtraction = float(x) - float(z)
        return print(subtraction)
    elif y == "/":
        div = float(x) / float(z)
        return print(div)
    else:
        multiplication = float(x) * float(z)
        return print(multiplication)

main()
