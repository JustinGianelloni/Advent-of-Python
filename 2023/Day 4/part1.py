from io import TextIOWrapper

INPUT: str = "input.txt"

def get_score(winners: list[int], picks: list[int]) -> int:
    count: int = 0
    for pick in picks:
        if pick in winners:
            count += 1
    if 0 <= count <= 1:
        return count
    return 2 ** (count -1)

def parse_picks(picks: str) -> list[int]:
    split: list[str] = picks.strip('\n').split(' ')
    result: list[int] = list()
    for number in split:
        if number.isnumeric():
            result.append(int(number))
    return result

def parse_winners(winners: str) -> list[int]:
    split: list[str] = winners.split(' ')
    result: list[int] = list()
    for number in split:
        if number.isnumeric():
            result.append(int(number))
    return result

def parse_line(line: str) -> int:
    card: list[str] = line.split(' | ')
    winners: list[int] = parse_winners(card[0].split(': ')[1])
    picks: list[int] = parse_picks(card[1])
    return get_score(winners, picks)

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
