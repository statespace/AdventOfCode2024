from collections import Counter

def main():
    with open("input_day1.txt") as f:
        data = f.read().splitlines()

    x = [[int(j) for j in i.split(' ') if j != ""] for i in data]

    total_dist = 0

    list_a = []
    list_b = []
    for i in x:
        list_a.append(i[0])
        list_b.append(i[1])
    list_a.sort()
    list_b.sort()

    for x,y in zip(list_a, list_b):
        total_dist += abs(x-y)
    
    print(f"Part1, total dist: {total_dist}")

    similarity = 0
    lookup_table = Counter(list_b)

    for i in list_a:
        similarity += i * lookup_table.get(i, 0)

    print(f"Part2, similarity: {similarity}")



if __name__ == "__main__":
    
    main()