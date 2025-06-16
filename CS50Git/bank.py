def main():
    userInput = str(input("Greeting: ")).lower().strip()
    hello = checkhello(userInput)



def checkhello(greeting):
    containsHello = greeting.startswith("hello")
    if containsHello:
        return print("$0")
    elif greeting.startswith("h"):
        return print("$20")
    else:
        return print("$100")


main()
