from io import TextIOWrapper

INPUT: str = "input.txt"

class Grid:

    pointer: list[int] = [ 0, 0 ]
    tracker: list[list[int]] = list()

    def __init__(self, file: list[str]) -> None:
        self.data: list[str] = file
        self.height: int = len(self.data)
        self.width: int = len(self.data[0])

    def get_next_char(self) -> str | None:
        if self.pointer[1] == self.width - 1:
            if self.pointer[0] == self.height - 1:
                return None
            self.pointer[0] += 1
            self.pointer[1] = 0
        else:
            self.pointer[1] += 1
        return self.data[self.pointer[0]][self.pointer[1]]

    def get_current_char(self) -> str:
        return self.data[self.pointer[0]][self.pointer[1]]

    def get_char_at(self, row: int, col: int) -> str | None:
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.data[row][col]
        return None

    def get_row(self) -> int:
        return self.pointer[0]

    def get_col(self) -> int:
        return self.pointer[1]

    def add_to_tracker(self, location: list[int]) -> None:
        self.tracker.append(location)

    def is_in_tracker(self, location: list[int]) -> bool:
        if location in self.tracker:
            return True
        return False

def look_right(grid: Grid, row: int, col: int) -> str | None:
    character: str | None = grid.get_char_at(row, col)
    if character is None:
        return None
    if not character.isnumeric():
        return None
    grid.add_to_tracker([row, col])
    right: str | None = look_right(grid, row, col+1)
    if right is not None:
        return character + right
    else:
        return character

def look_left(grid: Grid, row: int, col: int) -> str | None:
    character: str | None = grid.get_char_at(row, col)
    if character is None:
        return None
    if not character.isnumeric():
        return None
    grid.add_to_tracker([row, col])
    left: str | None = look_left(grid, row, col-1)
    if left is not None:
        return left + character
    else:
        return character

def expand_number(grid: Grid, row: int, col: int) -> int:
    if grid.is_in_tracker([row, col]):
        return 0
    grid.add_to_tracker([row, col])
    digits: str | None = grid.get_char_at(row, col)
    if digits is None:
        return 0
    right: str | None = look_right(grid, row, col+1)
    if right is not None:
        digits = digits + right
    left: str | None = look_left(grid, row, col-1)
    if left is not None:
        digits = left + digits
    return int(digits)

def check_for_number(grid: Grid, row: int, col: int) -> int:
    character: str | None = grid.get_char_at(row, col)
    if character is not None and character.isnumeric():
        return expand_number(grid, row, col)
    return 0

def check_symbol(grid: Grid) -> int:
    number: int = 0
    symbol: list[int] = [grid.get_row(), grid.get_col()]
    number += check_for_number(grid, symbol[0]+1, symbol[1])
    number += check_for_number(grid, symbol[0]+1, symbol[1]+1)
    number += check_for_number(grid, symbol[0], symbol[1]+1)
    number += check_for_number(grid, symbol[0]-1, symbol[1]+1)
    number += check_for_number(grid, symbol[0]-1, symbol[1])
    number += check_for_number(grid, symbol[0]-1, symbol[1]-1)
    number += check_for_number(grid, symbol[0], symbol[1]-1)
    number += check_for_number(grid, symbol[0]+1, symbol[1]-1)
    return number

def parse_line(line: str, symbols: list[str]) -> None:
    for character in line:
        if not character.isalnum() and not character == '.':
            if not character in symbols:
                symbols.append(character)

def parse_symbols(lines: list[str]) -> list[str]:
    symbols: list[str] = list()
    for line in lines:
        parse_line(line.strip('\n'), symbols)
    print(f"Symbols found: {symbols}")
    return symbols

def parse_page(file: TextIOWrapper) -> int:
    number: int = 0
    data: list[str] = file.readlines()
    grid: Grid = Grid(data)
    symbols = parse_symbols(data)
    while grid.get_next_char() is not None:
        if grid.get_current_char() in symbols:
            number += check_symbol(grid)
    return number

def main() -> None:
    file: TextIOWrapper = open(INPUT)
    answer: int = parse_page(file)
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()
