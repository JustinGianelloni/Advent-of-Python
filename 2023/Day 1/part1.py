from io import TextIOWrapper

INPUT: str = "input.txt"

def getNumber(digits: list[int]) -> int:
    num: str = str(digits[0]) + str(digits.pop())
    return int(num)

def parseLine(line: str) -> int:
    digits: list[int] = list()
    for character in line:
        if character.isnumeric():
            digits.append(int(character))
    return getNumber(digits)

def parsePage(file: TextIOWrapper) -> int:
    number: int = 0
    for line in file.readlines():
        number += parseLine(line)
    return number

def main() -> None:
    file: TextIOWrapper = open(INPUT)
    answer: int = parsePage(file)
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()
