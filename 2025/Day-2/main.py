def read_input():
    with open("input.txt") as file:
        input = file.read()
    
    return input.split(",")

def process_ranges(id_ranges):
    invalid_numbers = []
    for id_range in id_ranges:
        start, end = map(int, id_range.split("-"))
        print(f"Start: {start}, End: {end}")
        for num in range(start, end + 1):
            length = int(len(str(num)))
            if length % 2 == 0:
                e = length / 2
                q = num // 10 ** e
                r = num % 10 ** e
                if q == r:
                    invalid_numbers.append(num)

        print(f"Invalid Numbers so far: {invalid_numbers}")
    return invalid_numbers

# ---

id_ranges = read_input()
invalid_numbers = process_ranges(id_ranges)
print(f"Total Invalid Numbers: {sum(invalid_numbers)}")

# print(id_ranges)
# print(f"Invalid Numbers: {invalid_numbers}")

# string = "1010"
# print(string[0:2])