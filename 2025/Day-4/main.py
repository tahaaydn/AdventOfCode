def read_input(file_name):
    with open(file_name, "r") as f:
        input = f.readlines()
    return input

def part_one_two():
    global rolls
    lines = read_input("input.txt")
    line_length = len(lines[0].rstrip('\n'))
    
    def find_rolls(lines_map):
        x_map = []
        for i, r in enumerate(lines_map):
            sum = 0
            if r == '@':
                directions = [
                    (i-1, 'W'), (i+1, 'E'),
                    (line_length+i+1, 'S'), (i-1-line_length, 'N'),
                    (line_length+i+2, 'SE'), (line_length+i, 'SW'),
                    (-line_length+i, 'NE'), (i-2-line_length, 'NW')
                ]
                for idx, _ in directions:
                    if 0 <= idx < len(lines_map) and lines_map[idx] == '@':
                        sum += 1
            x_map.append((i, sum))
        return x_map
    
    def process_rolls(lines_map):
        global rolls
        x_map = find_rolls(lines_map)
        
        to_remove = [i for i, (pos, count) in enumerate(x_map) if lines_map[i] == '@' and count < 4]
        
        if not to_remove:
            return rolls
        
        lines_list = list(lines_map)
        for i in to_remove:
            lines_list[i] = 'x'
            rolls += 1
        
        lines_map = "".join(lines_list)
        return process_rolls(lines_map)
    
    final_map = process_rolls("".join(lines))
    return rolls
    
# ---

rolls = 0
result = part_one_two()
print(result)
