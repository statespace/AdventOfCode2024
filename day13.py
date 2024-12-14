import re
from tqdm import tqdm
import sympy as sp

def split_list_on_value(lst, value):
    chunks = []
    current_chunk = []

    for item in lst:
        if item == value:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = []
        else:
            current_chunk.append(item)

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def extract_numbers(s):
    return [int(num) for num in re.findall(r'\d+', s)]

def main():

    with open("input_day13.txt") as f:
        data = f.read().splitlines()

    data = split_list_on_value(data, "")

    values = []
    for i in data:
        values.append({
            'a': extract_numbers(i[0]),
            'b': extract_numbers(i[1]),
            'r': extract_numbers(i[2])
        })

    result = 0
    for i in values:
        #i = {'a': [94,34], 'b': [22,67], 'r': [8400, 5400]}
        steps_to_intersect = min(i['r'][0] // i['b'][0], i['r'][1] // i['b'][1])
        steps_to_intersect = min(100, steps_to_intersect)
        while steps_to_intersect >= 0:

            x_point = i['r'][0] - i['b'][0] * steps_to_intersect
            y_point = i['r'][1] - i['b'][1] * steps_to_intersect
            if x_point % i['a'][0] == 0 and y_point % i['a'][1] == 0:
                if (x_point // i['a'][0] > 100) or (x_point // i['a'][0] != y_point // i['a'][1]):
                    steps_to_intersect -= 1
                    continue
                result += (x_point // i['a'][0]) * 3 + steps_to_intersect
                break

            steps_to_intersect -= 1
    print(f"Part 1: {result}")
        

    x,y = sp.symbols('x,y')
    modifier = 10000000000000
    result = 0
    for i in tqdm(values):
        a = i['a']
        b = i['b']
        r = [i['r'][0] + modifier, i['r'][1] + modifier]

        solution = sp.solve(
            (sp.Eq(a[0] * x + b[0] * y, r[0]),
            sp.Eq(a[1] * x + b[1] * y, r[1]))
        )

        if solution[x] > 0 and solution[y] > 0 and isinstance(solution[x], sp.core.numbers.Integer) and isinstance(solution[y], sp.core.numbers.Integer):
            result += solution[x] * 3 + solution[y]
        


    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()