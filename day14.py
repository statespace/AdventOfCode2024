import re
from dataclasses import dataclass
from collections import defaultdict
from tqdm import tqdm

def extract_numbers(s):
    return [int(num) for num in re.findall(r'-?\d+', s)]

@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int
    x_constraint: int = 101
    y_constraint: int = 103

    def move(self):
        self.x = (self.x + self.dx) % self.x_constraint
        self.y = (self.y + self.dy) % self.y_constraint

    @property
    def quadrant(self):
        if self.x < self.x_constraint // 2 and self.y < self.y_constraint // 2:
            return 1
        elif self.x > self.x_constraint // 2 and self.y < self.y_constraint // 2:
            return 2
        elif self.x > self.x_constraint // 2 and self.y > self.y_constraint // 2:
            return 3
        elif self.x < self.x_constraint // 2 and self.y > self.y_constraint // 2:
            return 4
        else:
            return -1
        
def grid_state(robots: list[Robot], x_constraint: int, y_constraint: int):
    grid = [['.' for _ in range(x_constraint)] for _ in range(y_constraint)]
    for robot in robots:
        grid[robot.y][robot.x] = 'X'
    return grid

def display_robots(robots: list[Robot], x_constraint: int, y_constraint: int):
    grid = grid_state(robots, x_constraint, y_constraint)
    for row in grid:
        print("".join(row))

def grid_symmetry_score(grid):
    score = 0
    for i in range(len(grid) // 2):
        for j in range(len(grid[0])):
            if grid[i][j] == grid[-i-1][j] == 'X':
                score += 1
    return score

def main():

    with open("input_day14.txt") as f:
        data = f.read().splitlines()

    data = [Robot(*extract_numbers(i)) for i in data]

    seconds = 100
    counter = defaultdict(int)
    for robot in tqdm(data):
        for i in range(seconds):
            robot.move()
        counter[robot.quadrant] += 1

    print(f"Part1: {counter[1] * counter[2] * counter[3] * counter[4]}")

    # Part 2

    with open("input_day14.txt") as f:
        data = f.read().splitlines()
    data = [Robot(*extract_numbers(i)) for i in data]


    symmetry_scores = {}
    for move in tqdm(range(10000)):
        for robot in data:
            robot.move()
        grid = grid_state(data, 101, 103)
        #print(grid_symmetry_score(grid))
        score = grid_symmetry_score(grid)
        symmetry_scores[move] = score
        #if score == 139:
        #    display_robots(data, 101, 103)
        #    print(f"Move: {move}")
            
    
    print(f"Part2: {max(symmetry_scores.values())} @ key: {max(symmetry_scores, key=symmetry_scores.get)}")

    #display_robots(data, 101, 103)

if __name__ == "__main__":
    main()