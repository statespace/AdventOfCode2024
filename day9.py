from tqdm import tqdm

def main():

    # Part 1
    with open("input_day9.txt") as f:
        data = f.read()
    id_list = []
    switch = 1
    id_increment = 0
    for i in data:
        if switch == 1:
            for _ in range(int(i)):
                id_list.append(id_increment)
            switch = 0
            id_increment += 1
        else:
            for _ in range(int(i)):
                id_list.append(-1)
            switch = 1

    compact_list = []
    for idx,i in enumerate(id_list):
        if idx == len(id_list)-1:
            break   
        if i != -1: 
            compact_list.append(i)
        else:
            p = id_list.pop()
            while p == -1:
                p = id_list.pop()
            compact_list.append(p)

    result = 0
    for idx,val in enumerate(compact_list):
        result += idx*val

    print(f"Part 1 result: {result}")

    with open("input_day9.txt") as f:
        data = f.read()

    #data = "2333133121414131402"
    id_list = []
    switch = 1
    id_increment = 0
    for i in data:
        if switch == 1:
            for _ in range(int(i)):
                id_list.append(id_increment)
            switch = 0
            id_increment += 1
        else:
            for _ in range(int(i)):
                id_list.append(-1)
            switch = 1

    ids = list(set(id_list))[::-1]
    ids = [i for i in ids if i != -1]
    for i in tqdm(ids):
        # this is seriously slow
        indexes = [j for j, x in enumerate(id_list) if x == i]
        idxlen = len(indexes)
        start = 0
        searched = False
        while True:
            if -1 not in id_list[start:min(indexes)]:
                searched = True
                break
            
            start = id_list.index(-1, start)
            if len(id_list[start:]) < idxlen:
                break
            if all([id_list[start+j] == -1 for j in range(idxlen)]):
                break
            start += 1
        if searched:
            continue
        id_list[start:start+idxlen] = [i for _ in range(idxlen)]
        for remove in indexes:
            id_list[remove] = -1

    result = 0
    for idx,val in enumerate(id_list):
        if val != -1:
            result += idx*val
    print(f"Part2: {result}")

if __name__ == '__main__':
    main()