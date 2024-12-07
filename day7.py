from tqdm import tqdm

def find_factors(result: int, components: list[int]) -> bool:
    
    last_value = components[-1]

    if len(components) == 1:
        if result - last_value == 0:
            #print(f"Found: {result} - {last_value}")
            return True
        else:
            return False
    
    if result % last_value == 0:
        mult_branch = find_factors(result / last_value, components[:-1])
    else:
        mult_branch = False
    add_branch = find_factors(result - last_value, components[:-1])

    return mult_branch or add_branch

def three_branch(result: int, components: list[int]) -> bool:
    
    if len(components) == 1:
        if result - components[0] == 0:
            return True
        else:
            return False

    mult_branch = three_branch(result, [components[0] * components[1]] + components[2:])
    add_branch = three_branch(result, [components[0] + components[1]] + components[2:])
    concat_branch = three_branch(result, [int(str(components[0]) + str(components[1]))] + components[2:])

    return mult_branch or add_branch or concat_branch

def main():
    with open('input_day7.txt') as f:
        data = f.read().splitlines()

    proc_data = []
    for i in data:
        result, factors = i.split(':')
        factors = list(map(int, factors.strip().split(' ')))
        proc_data.append((int(result), factors))

    counter = 0
    for i in proc_data:
        if find_factors(*i):
            counter += i[0]

    print(f"Part 1: {counter}")

    counter = 0
    for i in tqdm(proc_data):
        if three_branch(*i):
            counter += i[0]

    print(f"Part 2: {counter}")

if __name__ == '__main__':
    main()