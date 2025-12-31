from math import sqrt
from collections import Counter

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.num_sets = size
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
    
    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep != jrep:
            self.parent[irep] = jrep
            self.num_sets -= 1

def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        return { i: tuple(int(x) for x in lines[i].split(",")) for i in range(len(lines)) }

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
            dist[(i, j)] = euclidean_distance(b1, b2)
    return dist

def solution():
    boxes = parse_input()
    dists = precompute_distances(boxes)
    dists = sorted(dists.items(), key=lambda x: x[1], reverse=True)
    circuits = UnionFind(len(boxes))
    while True:
        ids, _ = dists.pop()
        circuits.union(ids[0], ids[1])
        if circuits.num_sets == 1:
            print(boxes[ids[0]][0] * boxes[ids[1]][0])
            break

if __name__ == "__main__":
    solution()
