from pyparsing import Word, nums, Literal
def main():

    with open("input_day3.txt") as f:
        data = f.read().splitlines()

    multstr = Literal("mul")+"("+Word(nums)+","+Word(nums)+")"
    enable = Literal("do()")
    disable = Literal("don't()")

    parsestring = enable | disable | multstr

    total = 0
    do = True

    for match in parsestring.searchString(data):
        if match[0] == "do()":
            do = True
        elif match[0] == "don't()":
            do = False
        elif do:
            tmp = int(match[2]) * int(match[4])
            total += tmp

    print(total)

if __name__ == "__main__":
    main()