def main():
    userInput = str(input("what you want to say with emojies? "))
    emoji = faces(userInput)
    print(emoji)

def faces(emo):
    emo = emo.replace(':)', "🙂")
    emo = emo.replace(':(', "🙁")
    return emo

main()
