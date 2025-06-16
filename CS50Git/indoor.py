def main():
    userInput = str(input("What do you want to say with your indoor voice? "))
    lowerVoice = indoor(userInput)
    print(lowerVoice)

def indoor(say):
    return say.lower()


main()
