def read_input(file_name):
    with open(file_name, "r") as f:
        input = f.read().splitlines()
    return input

def part_one():
    input = read_input("input.txt")
    b = input.index('')
    ranges = [list(map(int, line.split('-'))) for line in input[:b]]
    fresh_ids = list(map(int, input[b+1:]))

    fresh_count = 0
    for fresh_id in fresh_ids:
        for r in ranges:
            if r[0] <= fresh_id <= r[1]:
                fresh_count += 1
                break

    return fresh_count

def part_two():
    input = read_input("input.txt")
    b = input.index('')
    ranges = [list(map(int, line.split('-'))) for line in input[:b]]
    
    ranges.sort()
    merged_ranges = []
    for r in ranges:
        if not merged_ranges or merged_ranges[-1][1] < r[0] - 1:
            merged_ranges.append(r)
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], r[1])

    # Can change part one to use merged ranges and binary search for optimization but shrug.

    fresh_id_count = sum([r[1] - r[0] + 1 for r in merged_ranges])

    return fresh_id_count

# ---

result_one = part_one()
result_two = part_two()

print(f"Part One Result: {result_one}\nPart Two Result: {result_two}")