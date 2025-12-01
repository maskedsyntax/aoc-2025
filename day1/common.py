def get_input(filename: str):
    with open(filename, "r") as file:
        return file.read().splitlines()
