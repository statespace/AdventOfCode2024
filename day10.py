from dataclasses import dataclass

@dataclass
class Node:
    value: int
    connections: list[tuple[int,int]]

def query_next(
    path: list[tuple[int,int]],
    coord_map: dict[tuple[int,int], Node], 
    current: tuple[int,int]
) -> list[list[tuple[int,int]]]:
    
    path.append(current)

    if coord_map[current].value == 9:
        return [path.copy()]

    paths = []
    for i in coord_map[current].connections:
        if coord_map[i].value - coord_map[current].value == 1:
            x = query_next(path, coord_map, i)
            paths.extend(x)

    path.pop()

    return paths
    
def main():
    with open("input_day10.txt") as f:
        data = f.read().splitlines()

    data = [[int(j) for j in i] for i in data]
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

    
    score_counter = 0
    trail_counter = 0
    for k,v in coord_map.items():
        if v.value == 0:
            path = query_next([], coord_map, k)
            summits = []
            for i in path:
                summits.append(i[-1])
            score_counter += len(set(summits))
            trail_counter += len(path)
    
    print(f"Part 1: {score_counter}")
    print(f"Part 2: {trail_counter}")
    

        


            


if __name__ == "__main__":
    main() 