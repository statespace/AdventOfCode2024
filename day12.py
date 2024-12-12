from dataclasses import dataclass
from tqdm import tqdm

@dataclass
class Node:
    value: str
    connections: list[tuple[int,int]]

def find_adjacent(
    start: tuple[int,int], 
    coord_map: dict[tuple[int,int], Node],
    visited: set[tuple[int,int]] = set()
) -> set[tuple[int,int]]:
    
    visited = visited.union({start})
    for i in coord_map[start].connections:
        if coord_map[start].value != coord_map[i].value:
            continue
        if i not in visited:
            visited = visited.union(find_adjacent(i, coord_map, visited))
    return visited

def calc_fence(
    nodes: set[tuple[int,int]], 
    coord_map: dict[tuple[int,int], Node]
) -> int:
    fence = 0
    for j in nodes:
        neighbors = len(set(coord_map[j].connections).intersection(nodes))
        fence += 4 - neighbors
    return fence

def discount_fence(
        nodes: set[tuple[int,int]],
        coord_map: dict[tuple[int,int], Node]
) -> int:
    
    checked = []
    discount = 0
    for i in nodes:
        for j in nodes:
            if (i, j) in checked:
                continue
            if i == j:
                continue
            if i not in coord_map[j].connections:
                continue
            
            # nodes are connected along the x-axis
            if i[1] == j[1]:
                # check if any of positions above or below are within nodes
                if not any([i in nodes for i in [(i[0], i[1]-1), (j[0], j[1]-1)]]):
                    discount += 1
                if not any([i in nodes for i in [(i[0], i[1]+1), (j[0], j[1]+1)]]):
                    discount += 1
            # y axis
            if i[0] == j[0]:
                if not any([i in nodes for i in [(i[0]-1, i[1]), (j[0]-1, j[1])]]):
                    discount += 1
                if not any([i in nodes for i in [(i[0]+1, i[1]), (j[0]+1, j[1])]]):
                    discount += 1

            checked.append((i, j))
            checked.append((j, i))
    
    return discount

            


def main():
    with open("input_day12.txt") as f:
        data = f.read().splitlines()

    height = len(data)
    width = len(data[0])

    coord_map = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            connections = []
            if j < width- 1:
                connections.append((i, j+1))
            if j > 0:
                connections.append((i, j-1))
            if i < height - 1:
                connections.append((i+1, j))
            if i > 0:
                connections.append((i-1, j))
            coord_map[(i, j)] = Node(data[i][j], connections)

    result = 0
    result2 = 0
    visited = set()
    for i in tqdm(coord_map):
        if i in visited:
            continue
        group = find_adjacent(i, coord_map)
        fence = calc_fence(group, coord_map)
        discount = discount_fence(group, coord_map)
        result += len(group) * fence
        result2 += len(group) * (fence - discount)
        #print(f"Value: {coord_map[i].value}, Area: {len(group)}, Fence: {fence}, Discount: {discount}")
        visited = visited.union(group)
    print(f"Part 1: {result}")
    print(f"Part 2: {result2}")
    


    #print(coord_map)

if __name__ == "__main__":
    main()