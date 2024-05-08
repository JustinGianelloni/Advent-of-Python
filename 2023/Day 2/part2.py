from io import TextIOWrapper

INPUT = "input.txt"

def parse_color(color: str, colors: dict[str, int]) -> None:
    split: list[str] = color.split(" ")
    if int(split[0]) > colors[split[1]]:
        colors[split[1]] = int(split[0])

def parse_reveal(reveal: str, colors: dict[str, int]) -> None:
    for color in reveal.split(", "):
        parse_color(color, colors)

def parse_line(line: str) -> int:
    reveals: list[str] = line.strip('\n').split(": ")[1].split("; ")
    colors: dict[str, int] = { "red": 0, "green": 0, "blue": 0 }
    for reveal in reveals:
        parse_reveal(reveal, colors)
    return colors["red"] * colors["green"] * colors["blue"]

def parse_page(file: TextIOWrapper) -> int:
    number: int = 0
    for line in file.readlines():
        number += parse_line(line)
    return number

def main():
    file: TextIOWrapper = open(INPUT)
    answer: int = parse_page(file)
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()
