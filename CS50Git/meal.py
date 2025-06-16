def main():
    userInput = input("What time is it? ")
    convert(userInput)
    hour, min = userInput.split(":")

    hour = int(hour)
    min = int(min)
    if (7 <= hour < 8):
        print("breakfast time")
    elif(hour == 8 and min == 00):
        print("breakfast time")
    elif 12 <= hour < 13:
        print("lunch time")
    elif(hour == 13 and min == 00):
        print("lunch time")
    elif 18 <= hour < 19:
        print("dinner time")
    elif hour == 19 and min == 00:
        print("dinner time")

def convert(hourMin):
    hour, min = hourMin.split(":")
    hour = int(hour)
    min = float(min)
    min = min/60
    return hour + min

if __name__ == "__main__":
    main()
