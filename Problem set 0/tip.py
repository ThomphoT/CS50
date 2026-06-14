def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid whole number.")


def calculate_tip(bill, percentage):
    return bill * percentage / 100


def main():
    bill = get_float("Bill amount: ")
    percentage = get_float("Tip percentage: ")
    people = get_int("Number of people: ")

    tip = calculate_tip(bill, percentage)
    total = bill + tip
    each_person = total / people

    print(f"Tip: {tip:.2f}")
    print(f"Total: {total:.2f}")
    print(f"Each person pays: {each_person:.2f}")


main()
