import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        for attempt in range(3):
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == answer:
                    score += 1
                    break
                print("EEE")
            except ValueError:
                print("EEE")

            if attempt == 2:
                print(f"{x} + {y} = {answer}")

    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)
    raise ValueError


if __name__ == "__main__":
    main()
