DIAL_START = 50

def read_input(file_path):
    with open(file_path) as file:
        input = file.read().splitlines()

    rotations = []

    for line in input:
        direction = line[0]
        amount = line[1:]
        if direction == 'L':
            rotations.append(-int(amount))
        else:
            rotations.append(int(amount))
    return rotations

def count_zeros(rotations):
    position = DIAL_START
    zeros = 0
    for rotation in rotations:
        new_position = position + rotation
        if new_position > 0:
            zeros += new_position // 100
        elif new_position == 0:
            zeros += 1
        else:
            zeros += (((100 - position) % 100) + abs(rotation)) // 100
        position = (position + rotation) % 100
    return zeros

zero_count = count_zeros(read_input('input.txt'))

print(f"Zero Count: {zero_count}")