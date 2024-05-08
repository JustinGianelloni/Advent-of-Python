from io import TextIOWrapper

INPUT: str = "input.txt"
WORDS: dict[str, int] = {
    "oneight": 18,
    "twone": 21,
    "threeight": 38,
    "fiveight": 58,
    "sevenine": 79,
    "eightwo": 82,
    "eighthree": 83,
    "nineight": 98,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def replace_words(line: str) -> str:
    for word, value in WORDS.items():
        line = line.replace(word, str(value))
    return line

def get_number(digits: list[int]) -> int:
    num: str = str(digits[0]) + str(digits.pop())
    return int(num)

def parse_line(line: str) -> int:
    digits: list[int] = list()
    line = replace_words(line)
    for character in line:
        if character.isnumeric():
            digits.append(int(character))
    return get_number(digits)

def parse_page(file: TextIOWrapper) -> int:
    number: int = 0
    for line in file.readlines():
        number += parse_line(line)
    return number

def main() -> None:
    file: TextIOWrapper = open(INPUT)
    answer: int = parse_page(file)
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()
