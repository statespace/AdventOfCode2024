from pyparsing import Literal

def main():

    with open("input_day4.txt") as f:
        data = f.read().splitlines()

    # Part 1

    xmas = Literal("XMAS")

    counter = 0

    # left
    for match in xmas.search_string(data):
        counter += 1

    # right
    right = [i[::-1] for i in data]
    for match in xmas.search_string(right):
        counter += 1

    # down
    down =list(map(list, zip(*data)))
    down = [''.join(i) for i in down]
    for match in xmas.search_string(down):
        counter += 1

    # up
    up = [i[::-1] for i in down]
    for match in xmas.search_string(up):
        counter += 1

    # diagonals
    def get_diagonals(matrix):
        diagonals = []

        # Top-left to bottom-right diagonals
        for p in range(-len(matrix) + 1, len(matrix)):
            diagonals.append([matrix[i][i - p] for i in range(max(p, 0), min(len(matrix), len(matrix) + p))])

        # Top-right to bottom-left diagonals
        for p in range(len(matrix) * 2 - 1):
            diagonals.append([matrix[i][p - i] for i in range(max(0, p - len(matrix) + 1), min(len(matrix), p + 1))])

        diagonals = [''.join(i) for i in diagonals]
        return diagonals
    
    diagonals = get_diagonals(data)
   
    
    for match in xmas.search_string(diagonals):
        counter += 1

    # reverse diagonals
    revdiagonals = [i[::-1] for i in diagonals]
    for match in xmas.search_string(revdiagonals):
        counter += 1

    print(f"Part 1, total counter: {counter}")

    # Part 2

    # moving window of 3 x 3 over the matrix
    counter = 0
    for i in range(len(data[0]) - 2):
        for j in range(len(data) - 2):
            window = [data[j][i:i+3], data[j+1][i:i+3], data[j+2][i:i+3]]

            diag = get_diagonals(window)
            if diag[2] in ["MAS", "SAM"] and diag[7] in ["MAS", "SAM"]:
                counter += 1

    print(f"Part 2, total counter: {counter}")

if __name__ == "__main__":
    main()