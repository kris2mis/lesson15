def check_vowel(character):
    character = character.upper()
    vowels = ["a", "o", "e", "i", "u"]
    return character in vowels


def main():
    character = input("Input the letter: ")
    result = check_vowel(character)
    msg = f"It is {result}"
    print(msg)


main()
