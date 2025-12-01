from common import get_input

input = get_input("input.txt")

dial = 50
password = 0

for rotation in input:
    print(rotation)
    if rotation[0] == "L":
        dial = (dial - int(rotation[1:])) % 100
    else:
        dial = (dial + int(rotation[1:])) % 100
    if dial == 0:
        password += 1

    print(dial)

print(password)
