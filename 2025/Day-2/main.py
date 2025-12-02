def read_input():
    with open("input.txt") as file:
        input = file.read().split(",")
    return input

def process_ranges(id_ranges):
    invalid_numbers = []
    for id_range in id_ranges:
        start, end = map(int, id_range.split("-"))
        for num in range(start, end + 1):
            length = len(str(num))

            for i in range(1, length//2 + 1):
                if length % i != 0:
                    continue
                r = length // i

                q = sum((10**(i*j) for j in range(0, r)))
                if num % q == 0:
                    invalid_numbers.append(num)
                    print(f"Checking {num} with q={q}, length={length}, i={i}, r={r}, length//2={length//2}")
                    break
    return invalid_numbers

# ---

id_ranges = read_input()
invalid_numbers = process_ranges(id_ranges)

print(f"Total Invalid Numbers: {sum(invalid_numbers)}")