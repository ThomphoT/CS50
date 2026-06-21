import emoji


def main():
    # Convert typed emoji codes or aliases into real emoji characters.
    text = input("Input: ")
    print(emoji.emojize(text, language="alias"))


main()
