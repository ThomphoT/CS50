import inflect


def main():
    engine = inflect.engine()
    names = []

    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            break

    print(f"Adieu, adieu, to {engine.join(names)}")


main()
