items = {}

while True:
    try:
        item = input().strip().casefold()
    except EOFError:
        break

    items[item] = items.get(item, 0) + 1

for item in sorted(items):
    print(f"{items[item]} {item.upper()}")
