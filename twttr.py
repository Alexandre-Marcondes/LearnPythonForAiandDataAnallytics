def main():
    userInput = input("Input: ")
    vowl_less = no_vowels(userInput)
    print(vowl_less)

def no_vowels(sentence):
    no_vowel = ""
    for cons in sentence:
        vow = cons.lower()
        if vow == "a" or vow == "e" or vow == "i" or vow == "o" or vow == "u":
            no_vowel = no_vowel
        else:
            no_vowel = no_vowel + cons

    return no_vowel

main()
