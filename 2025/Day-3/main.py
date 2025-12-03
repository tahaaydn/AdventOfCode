def part_one():
    output = 0
    for bank in banks:
        n1, n2 = 0, 0
        for i, n in enumerate(bank):
            if int(n) > n1:
                if i != len(bank) - 1:
                    n1 = int(n)
                    n1i = i
        
        for n in bank[n1i+1:]:
            if int(n) > n2:
                n2 = int(n)

        lj = str(n1) + str(n2)
        output += int(lj)
    return output

def part_two():
    output = 0
    for bank in banks:
        joltage, lastPosition = '', 0
        while len(joltage) < 12:
            nextBattery = max(bank[lastPosition:len(bank)-(11-len(joltage))])
            joltage += str(nextBattery)
            lastPosition = bank.index(str(nextBattery), lastPosition)+1
        output += int(joltage)
    return output

# ---

with open("input.txt", "r") as f:
    banks = f.read().splitlines()

result_one = part_one()
result_two = part_two()
print(f"Result of Part One: {result_one}\nResult of Part Two: {result_two}")