from enum import Enum
from io import TextIOWrapper

INPUT: str = "input.txt"
COLORS: dict[str, int] = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_color_possible(color: str) -> bool:
    split: list[str] = color.split(" ")
    if int(split[0]) > COLORS[split[1]]:
        return False
    return True

def is_reveal_possible(reveal: str) -> bool:
    for color in reveal.split(", "):
        if not is_color_possible(color):
            return False
    return True

def is_game_possible(game: str) -> bool:
    for reveal in game.split("; "):
        if not is_reveal_possible(reveal):
            return False
    return True

def parse_line(line: str) -> int:
    split: list[str] = line.strip('\n').split(": ")
    game: list[str] = split[0].split(" ")
    if is_game_possible(split[1]):
        return int(game[1])
    return 0

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
