from math import prod
from itertools import chain
import re

file_name = 'input.txt'

def read_input(file_name: str) -> list[str]:
    with open(file_name, 'r') as f:
        return f.readlines()
    
def calc_sum(input: list) -> int:
    result = 0
    for c in input:
        opr = c[-1]
        if opr == '+':
            result += sum(map(int, c[:-1]))
        elif opr == '*':
            result += prod(map(int, c[:-1]))
    return result

def part_one():
    input = read_input(file_name)
    input = list(map(list, zip(*[r.split() for r in input])))
    return calc_sum(input)

def part_two():
    input = read_input(file_name)
    input = list(zip(*input))
    input = list(chain.from_iterable(reversed(input)))
    input = "".join(input)
    input = re.findall(r"(?<![\\*+]).*?[\\*+]", input)
    input = [re.findall(r"\d+|[*+]", i) for i in input]
    return calc_sum(input)

if __name__ == '__main__':
    print(f'Part One: {part_one()}')
    print(f'Part Two: {part_two()}')
    # assert part_one() == 4277556
    # assert part_two() == 3263827