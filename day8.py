def locate(data: list[str], char: str) -> list[tuple[int, int]]:
    return [(x, y) for y, row in enumerate(data) for x, col in enumerate(row) if col == char]

def get_unique_pairs(lst):
    unique_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            pair = (lst[i], lst[j])
            unique_pairs.add(pair)
    return list(unique_pairs)

def set_value_at_index(input: list[str], x: int, y: int, value: str) -> None:
    data = input.copy()
    data[y] = data[y][:x] + value + data[y][x+1:]
    return data

def antinodes(node1: tuple[int, int], node2: tuple[int, int]) -> list[tuple[int, int]]:

    x_diff = node1[0] - node2[0]
    y_diff = node1[1] - node2[1]

    antinode1 = (node1[0] + x_diff, node1[1] + y_diff)
    antinode2 = (node2[0] - x_diff, node2[1] - y_diff)

    return [antinode1, antinode2]

def antinode_line(
        node1: tuple[int, int], 
        node2: tuple[int, int], 
        width: int,
        height: int
    ) -> list[tuple[int, int]]:
    
    x_diff = node1[0] - node2[0]
    y_diff = node1[1] - node2[1]

    antinodes = []
    for i in range(0, int(max(width, height) / min(abs(x_diff), abs(y_diff)))):
        # this does create a few extras, but it's not a big deal
        antinode1 = (node1[0] + x_diff * i, node1[1] + y_diff * i)
        antinodes.append(antinode1)
        antinode2 = (node2[0] - x_diff * i, node2[1] - y_diff * i)
        antinodes.append(antinode2)

    # filter out any antinodes that are out of bounds
    antinodes = [i for i in antinodes if i[0] >= 0 and i[1] >= 0 and i[0] < width and i[1] < height]

    return antinodes

    


def main():
    with open('input_day8.txt') as f:
        data = f.read().splitlines()

    unique_chars = set()
    for i in data:
        unique_chars.update(i)

    width = len(data[0])
    height = len(data)

    p1_antinodes = []

    for i in unique_chars:
        if i == ".":
            continue
        #print(f"Locating {i}: {locate(data, i)}")
        locations = locate(data, i)
        pairs = get_unique_pairs(locations)
        for j in pairs:
            p1_antinodes.extend(antinodes(*j))
    
    p1_antinodes = [i for i in p1_antinodes if i[0] >= 0 and i[1] >= 0 and i[0] < width and i[1] < height]
    print(f"Part 1: {len(set(p1_antinodes))}")

    p2_antinodes = []

    for i in unique_chars:
        if i == ".":
            continue
        #print(f"Locating {i}: {locate(data, i)}")
        locations = locate(data, i)
        pairs = get_unique_pairs(locations)
        for j in pairs:
            tmp = antinode_line(*j, width, height)
            p2_antinodes.extend(tmp)

    print(f"Part 2: {len(set(p2_antinodes))}")

    # for i in p2_antinodes:
    #     data = set_value_at_index(data, i[0], i[1], "#")
    # print("\n".join(data))

    



if __name__ == '__main__':
    main()