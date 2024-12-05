def main():
    with open("input_day5_p1.txt") as f:
        rules = f.read().splitlines()

    with open("input_day5_p2.txt") as f:
        updates = f.read().splitlines()
        updates = [[int(j) for j in i.split(",")] for i in updates]

    result = 0
    incorrect = []

    for i in updates:
        correct = True
        for j in rules:
            precedes, follows = tuple([int(x) for x in j.split("|")])
            if precedes not in i or follows not in i:
                continue
            if i.index(precedes) > i.index(follows):
                correct = False
        if correct:
            result += i[int(len(i) / 2)]
        else:
            incorrect.append(i)

    print(f"Part 1: {result}")

    result = 0
    for i in incorrect:
        correct = False
        while not correct:
            modified = False
            for j in rules:
                precedes, follows = tuple([int(x) for x in j.split("|")])
                if precedes not in i or follows not in i:
                    continue
                if i.index(precedes) > i.index(follows):
                    i[i.index(precedes)], i[i.index(follows)] = i[i.index(follows)], i[i.index(precedes)]
                    modified = True
            if not modified:
                correct = True
                result += i[int(len(i) / 2)]

    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()