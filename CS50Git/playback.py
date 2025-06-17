def main():
    userInput = str(input("what you want to say at a slower speed? "))
    slower = playback(userInput)
    print(slower)

def playback(userInput):
    return userInput.replace(" ", "...")

main()
