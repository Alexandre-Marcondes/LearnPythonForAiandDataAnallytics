def main():
    userNum = int(input("Please enter the mass to find out the energy needed: "))
    energy = formula(userNum)
    print(f"E is: {energy}")

def formula(mass):
    E = mass * pow(300000000, 2)
    return E

main()

