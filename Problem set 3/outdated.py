months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        try:
            date = input()
            print(convert(date))
            break
        except (ValueError, IndexError):
            continue


def convert(date):
    if "/" in date:
        month, day, year = date.split("/")
    else:
        month_name, day_year = date.split(" ", 1)
        day, year = day_year.replace(",", "").split()
        month = str(months.index(month_name) + 1)

    month = int(month)
    day = int(day)
    year = int(year)
    return f"{year:04}-{month:02}-{day:02}"


if __name__ == "__main__":
    main()
