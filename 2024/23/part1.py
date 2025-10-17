from collections import defaultdict
from queue import Queue

def parse_input():
    edges = set()
    nodes = set()
    g = defaultdict(list)
    with open("input.txt") as f:
        for line in f:
            u, v = line.strip().split("-")
            nodes.add(u)
            nodes.add(v)
            edges.add((u,v))
            edges.add((v,u))
            g[u].append(v)
            g[v].append(u)
    return g, nodes, edges

def bfs(g, s):
    q = Queue()
    q.put_nowait([s])
    three_cliques = set()
    while not q.empty():
        path = q.get_nowait()
        node = path[-1]
        if node == s and len(path) == 4:
            three_cliques.add(tuple(sorted(path[1:])))
            continue
        elif len(path) == 4:
            continue
        for neighbour in g[node]:
            q.put_nowait(path + [neighbour])
    return three_cliques

def find_three_cliques(g, nodes):
    t_nodes = list(filter(lambda x: x.startswith("t"), nodes))
    three_cliques = set()
    for tnode in t_nodes:
        three_cliques.update(bfs(g, tnode))
    return len(three_cliques)

def solution():
    g, nodes, edges = parse_input()
    num_three_cliques = find_three_cliques(g, nodes)
    print(num_three_cliques)

if __name__ == "__main__":
    solution()
