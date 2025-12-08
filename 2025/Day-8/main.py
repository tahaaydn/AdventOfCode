import itertools
import math

def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()
    
def merge_circuits(circuits):
    while True:
        prev_count = len(circuits)
        new_circuits = []
        for circuit in circuits:
            for existing in new_circuits:
                if circuit & existing:
                    existing.update(circuit)
                    break
            else:
                new_circuits.append(circuit)
        circuits = new_circuits
        if len(circuits) == prev_count:
            break
    return circuits
    
def part_one():
    global sorted_edges

    points = read_input("input.txt").splitlines()
    points = [tuple(map(int, point.split(','))) for point in points]
    
    def get_dist(p: tuple, q: tuple):
        return math.sqrt(math.pow(p[0] - q[0], 2) + 
                         math.pow(p[1] - q[1], 2) + 
                         math.pow(p[2] - q[2], 2))    
    
    edges = {}
    for i in range(len(points) - 1):
        for j in range(len(points) - 1 - i):
            distance = get_dist(points[i], points[j + i + 1])
            edges[i, j + i + 1] = distance
    
    sorted_edges = dict(sorted(edges.items(), key=lambda item: item[1]))
    N = 1000
    top_values = dict(list(itertools.islice(sorted_edges.items(), N)))

    circuits = [{k1, k2} for k1, k2 in top_values.keys()]
    circuits = merge_circuits(circuits)
    sorted_lengths = sorted([len(circuit) for circuit in circuits], reverse=True)[:3]
    return math.prod(sorted_lengths)

def part_two():
    points = read_input("input.txt").splitlines()
    points = [tuple(map(int, point.split(','))) for point in points]

    connections = sorted_edges.keys()
    circuits = []
    for connection in connections:
        k1, k2 = connection
        circuits.append({k1, k2})
        circuits = merge_circuits(circuits)
        if len(circuits) == 1 and len(circuits[0]) == len(points):
            last_connection = connection
            break
    
    [x1, x2] = last_connection
    return points[x1][0] * points[x2][0]

if __name__ == "__main__":
    print(f'Part One: \n{part_one()}')
    print(f'Part Two: \n{part_two()}')