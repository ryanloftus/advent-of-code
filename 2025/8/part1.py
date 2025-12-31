from math import sqrt
from collections import Counter

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
    
    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        self.parent[irep] = jrep

class Box:
    def __init__(self, id, loc):
        self.id = id
        self.loc = loc

def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        return [Box(i, tuple(int(x) for x in lines[i].split(","))) for i in range(len(lines))]

def euclidean_distance(b1, b2):
    x1, y1, z1 = b1
    x2, y2, z2 = b2
    return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def precompute_distances(boxes):
    dist = dict()
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            b1 = boxes[i]
            b2 = boxes[j]
            dist[(b1.id, b2.id)] = euclidean_distance(b1.loc, b2.loc)
    return dist

def solution():
    boxes = parse_input()
    dists = precompute_distances(boxes)
    dists = sorted(dists.items(), key=lambda x: x[1], reverse=True)
    connections = 1000
    circuits = UnionFind(len(boxes))
    for _ in range(connections):
        ids, _ = dists.pop()
        circuits.union(ids[0], ids[1])
    top_circuit_sizes = sorted(Counter([circuits.find(x) for x in range(len(boxes))]).items(), key=lambda x: x[1], reverse=True)[:3]
    answer = top_circuit_sizes[0][1] * top_circuit_sizes[1][1] * top_circuit_sizes[2][1]
    print(answer)

if __name__ == "__main__":
    solution()
