from common import get_input

input = get_input("input.txt")
# input = ["R1050"]

dial = 50
password = 0

for rotation in input:
    num = int(rotation[1:])
    mult = 0
    if num >= 100:
        mult = num // 100

    num = num % 100

    if rotation[0] == "L":
        check = dial - num
        if check <= 0 and dial != 0:
            password = password + 1
        dial = (check) % 100

    else:
        check = dial + num
        if check >= 100:
            password += 1
        dial = (check) % 100
    password += mult

print(password)
