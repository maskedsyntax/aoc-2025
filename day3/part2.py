from typing import List


def get_input(filename: str):
    with open(filename, "r") as file:
        return file.read().splitlines()


# input = get_input("example.txt")
input = get_input("input.txt")


ans = 0


def nullifyrest(idx: int, arr: List) -> List:
    for i in range(idx, len(arr)):
        arr[i] = "0"
    return arr


for bank in input:
    num = ["0" for _ in range(12)]
    # print(num)
    idx = 0
    for i in range(len(bank)):
        for j in range(len(num)):
            if bank[i] > num[j] and i <= len(bank) - 1 - (11 - j):
                num[j] = bank[i]
                nullifyrest(j + 1, num)
                break

    print(num)
    ans += int("".join(num))

print(ans)

"""
j=0 => i > 88
j=1 => 89
j=2 => 90
.
.
.
j=11 => 0
"""
