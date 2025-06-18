def main():
    print("Amount Due: 50 cents")
    userInput = int(input("Insert Coin: "))
    change(userInput)

def change(coin):
    amount_due = 50
    remainder = 50
    while amount_due != 0:
        if coin == 25 or coin == 10 or coin == 5:
            amount_due = amount_due - coin
            remainder = amount_due
            if remainder <= 0:
                break
            else:
                print(f"Amount due: {amount_due}")
                coin = int(input("Insert Coin: "))
        else:
            print(f"Amount due: {amount_due}")
            coin = int(input("Insert Coin: "))


    return print(f"Change Owed: {-1 * remainder} ")

main()
