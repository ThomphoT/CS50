text = input()
output = ""

for character in text:
    if character.lower() not in "aeiou":
        output += character

print(output)
