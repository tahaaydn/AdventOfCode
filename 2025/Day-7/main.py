def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()

def part_one():
    lines = read_input('test.txt').splitlines()
    lines_str = list(map(list, lines))

    splits = 0
    for idx1, line in enumerate(lines_str):
        for idx2, i in enumerate(line):
            if i == 'S':
                lines_str[idx1+1][idx2] = '|'
            elif lines_str[idx1-1][idx2] == '|':
                if i == '^':
                    lines_str[idx1][idx2-1] = '|'
                    lines_str[idx1][idx2+1] = '|'
                    splits += 1
                elif i == '.':
                    lines_str[idx1][idx2] = '|'
    return splits

def part_two():
    lines = read_input('input.txt').splitlines()
    lines_str = list(map(list, lines))

    for idx1, line in enumerate(lines_str):
        for idx2, i in enumerate(line):
            if i == 'S':
                lines_str[idx1+1][idx2] = 1

            if i == '.':
                if lines_str[idx1-1][idx2] not in ('.', '^'):
                    lines_str[idx1][idx2] = lines_str[idx1-1][idx2]

            if i == '^':
                if lines_str[idx1-1][idx2] != '.':
                    lines_str[idx1][idx2-1] = lines_str[idx1-1][idx2] if lines_str[idx1][idx2-1] == '.' else lines_str[idx1-1][idx2] + lines_str[idx1][idx2-1]
                    lines_str[idx1][idx2+1] = lines_str[idx1-1][idx2] if lines_str[idx1][idx2+1] == '.' else lines_str[idx1-1][idx2] + lines_str[idx1][idx2+1]
                    
                    # We already iterated over the left side so we don't need to do it again. If we do we won't get correct result.
                    # lines_str[idx1][idx2-1] = lines_str[idx1][idx2-1] + lines_str[idx1-1][idx2-1] if lines_str[idx1-1][idx2-1] != '.' else lines_str[idx1][idx2-1]
                    lines_str[idx1][idx2+1] = lines_str[idx1][idx2+1] + lines_str[idx1-1][idx2+1] if lines_str[idx1-1][idx2+1] != '.' else lines_str[idx1][idx2+1]               
    return sum([i for i in lines_str[-1] if isinstance(i, int)])

if __name__ == "__main__":
    print(f'Part One: \n{part_one()}')
    print(f'Part Two: \n{part_two()}')