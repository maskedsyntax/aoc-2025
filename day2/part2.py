def get_input(filename: str):
    with open(filename, "r") as file:
        return file.read().splitlines()


# input = get_input("input.txt")[0]
input = get_input("example.txt")[0]
ranges = input.split(",")

ans = 0
for r in ranges:
    x, y = map(int, r.split("-"))
    for i in range(x, y + 1):
        num = str(i)
        l = len(num)
        for j in range(2, l + 1):
            if l % j == 0:
                nr = l // j
                if num[:nr] * j == num:
                    ans += i
                    break

print(ans)
