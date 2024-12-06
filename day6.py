import pyparsing as pp
from dataclasses import dataclass
from tqdm import tqdm

def get_position(input: list[str], pos: tuple[int, int]) -> str:
    return input[pos[1]][pos[0]]
    
@dataclass
class Path:
    path: list[tuple[int, int], str]
    has_loop: bool

    @property
    def positions(self) -> list[tuple[int, int]]:
        return [i[0] for i in self.path]

@dataclass
class Guard:
    pos: tuple[int, int]
    direction: str

    def turn_right(self) -> None:
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"

    def next_step(self) -> tuple[int, int]:
        x,y = self.pos
        if self.direction == "^":
            return (x, y-1)
        elif self.direction == "v":
            return (x, y+1)
        elif self.direction == "<":
            return (x-1, y)
        elif self.direction == ">":
            return (x+1, y)
        
    def move(self) -> None:
        self.pos = self.next_step()

    @property
    def state(self) -> tuple[tuple[int, int], str]:
        return (self.pos, self.direction)


def locate_guard(input: list[str]) -> Guard:
    guard = pp.Literal("^") | pp.Literal("v") | pp.Literal("<") | pp.Literal(">")
    for y, row in enumerate(input):
        for x, col in enumerate(row):
            if guard.matches(col):
                return Guard(pos = (x, y), direction=get_position(input, (x, y)))
    raise ValueError("No guard found")
    
def simulate_path(input: list[str], check_loops = False) -> Path:
    g = locate_guard(input)
    path = [g.state]
    has_loop = False
    while True:
        if has_loop:
            break
        next_step = g.next_step()
        if next_step[0] < 0 or next_step[1] < 0 or next_step[0] >= len(input[0]) or next_step[1] >= len(input):
            break
        if get_position(input, next_step) == "#":
            g.turn_right()
        else:
            g.move()
            if check_loops and g.state in path:
                has_loop = True
                break
            path.append(g.state)
    return Path(path, has_loop)

def set_value_at_index(input: list[str], x: int, y: int, value: str) -> None:
    data = input.copy()
    data[y] = data[y][:x] + value + data[y][x+1:]
    return data

def main():

    # Part 1

    with open("input_day6.txt") as f:
        data = f.read().splitlines()

    path = simulate_path(data)
    print(f"Part 1 result: {len(set(path.positions))}")

    # Part 2
    # condition for loop is when two consecutive steps are the same as any other two steps

    counter = 0

    for x, y in tqdm(set(path.positions)):
        if (x, y) == locate_guard(data).pos or get_position(data, (x, y)) == "#":
            continue
        new_data = set_value_at_index(data, x, y, "#")
        new_path = simulate_path(new_data, True)
        if new_path.has_loop:
            counter += 1
            #print(f"Loop found at ({x}, {y})")

    print(f"Part 2 result: {counter}")

if __name__ == "__main__":
    main()