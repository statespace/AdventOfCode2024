from tqdm import tqdm
from collections import defaultdict

def apply_rules(x: int) -> list[int]:
    if x == 0:
        return [1]
    elif len(str(x)) % 2 == 0:
        splitidx = int(len(str(x)) / 2)
        x1 = str(x)[0:splitidx]
        x2 = str(x)[splitidx:]
        return [int(x1), int(x2)]
    else:
        return [x * 2024]
    


def main():

    with open("input_day11.txt") as f:
        data = f.read()

    data = [int(i) for i in data.split(' ')]

    for _ in range(25):
        container = []
        for i in data:
            container.extend(apply_rules(i))
        data = container

    print(f"Part 1: {len(data)}")

    with open("input_day11.txt") as f:
        data = f.read()

    data = [int(i) for i in data.split(' ')]

    init_container = defaultdict(int)
    for i in data:
        init_container[i] += 1


    for _ in tqdm(range(75)):
        container = defaultdict(int)
        for x in init_container:
            if x == 0:
                container[1] += init_container[x]
            elif len(str(x)) % 2 == 0:
                splitidx = int(len(str(x)) / 2)
                x1 = int(str(x)[:splitidx])
                x2 = int(str(x)[splitidx:])
                container[x1] += init_container[x]
                container[x2] += init_container[x]
            else:
                container[x * 2024] += init_container[x]
        init_container = container

    result = 0
    for i in init_container:
        result += init_container[i]

    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()