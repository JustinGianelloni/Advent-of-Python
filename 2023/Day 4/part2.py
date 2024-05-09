from io import TextIOWrapper

INPUT: str = "input.txt"

def get_score(winners: list[int], picks: list[int]) -> int:
    count: int = 0
    for pick in picks:
        if pick in winners:
            count += 1
    return count

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

def add_cards(cards: list[int], amount: int, current_card: int) -> None:
    i: int = 1
    while i <= amount and current_card + i < len(cards):
        cards[current_card + i] += 1 * cards[current_card]
        i += 1

def parse_line(line: str, cards: list[int], current_card: int):
    card: list[str] = line.split(' | ')
    winners: list[int] = parse_winners(card[0].split(': ')[1])
    picks: list[int] = parse_picks(card[1])
    score: int = get_score(winners, picks)
    add_cards(cards, score, current_card)

def sum_cards(cards: list[int]) -> int:
    total: int = 0
    for card in cards:
        total += card
    return total

def parse_page(file: TextIOWrapper) -> int:
    lines: list[str] = file.readlines()
    cards: list[int] = [1] * len(lines)
    current_card: int = 0
    for line in lines:
        parse_line(line, cards, current_card)
        current_card += 1
    return sum_cards(cards)

def main() -> None:
    file: TextIOWrapper = open(INPUT)
    answer: int = parse_page(file)
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()
