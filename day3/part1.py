def get_input(filename: str):
    with open(filename, "r") as file:
        return file.read().splitlines()


# input = get_input("example.txt")
input = get_input("input.txt")


ans = 0

print(input)

for bank in input:
    b1 = "0"
    b2 = "0"
    idx = 0
    for i, b in enumerate(bank):
        if b > b1 and i != len(bank) - 1:
            b1 = b
            idx = i

    for i in range(idx + 1, len(bank)):
        if bank[i] > b2:
            b2 = bank[i]

    print(b1, b2)
    ans += int(b1) * 10 + int(b2)

print(ans)
