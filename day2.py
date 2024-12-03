def main():
    with open("input_day2.txt") as f:
        data = f.read().splitlines()

    data = [[int(j) for j in i.split(' ')] for i in data]

    counter = 0
    for i in data:
        if is_decreasing(i) or is_increasing(i):
            counter += 1

    print(f"Part1, counter: {counter}")

    counter = 0
    for i in data:
        if is_decreasing(i, 1) or is_increasing(i, 1):
            counter += 1

    print(f"Part2, counter: {counter}")

def is_decreasing(x: list[int], tolerance = 0) -> bool:
    for i in range(len(x)-1):
        if (x[i] <= x[i+1]) or (x[i] - x[i+1] > 3):
            if tolerance == 0:
                return False
            else:
                for j in range(len(x)):
                    if is_decreasing(x[:j] + x[j+1:]):
                        return True
            return False
    #print(f"Decreasing: {x}")
    return True

def is_increasing(x: list[int], tolerance = 0) -> bool:
    for i in range(len(x)-1):
        if (x[i] >= x[i+1]) or (x[i+1] - x[i] > 3):
            if tolerance == 0:
                return False
            else:
                for j in range(len(x)):
                    if is_increasing(x[:j] + x[j+1:]):
                        return True
            return False
    #print(f"Increasing: {x}")
    return True



if __name__ == "__main__":
    main()