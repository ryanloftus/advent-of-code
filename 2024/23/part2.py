from collections import defaultdict

def parse_input():
    nodes = set()
    g = defaultdict(set)
    with open("input.txt") as f:
        for line in f:
            u, v = line.strip().split("-")
            nodes.add(u)
            nodes.add(v)
            g[u].add(v)
            g[v].add(u)
    return g, nodes

def bron_kerbosch(g, R, P, X):
    cliques = set()
    if len(P) == 0 and len(X) == 0:
        cliques.add(tuple(R))
    while P:
        v = P.pop()
        other_cliques = bron_kerbosch(g, R.union({v}), P.intersection(g[v]), X.intersection(g[v]))
        for other_clique in other_cliques:
            cliques.add(tuple(other_clique))
        X.add(v)
    return cliques

def find_largest_clique(g, nodes):
    cliques = bron_kerbosch(g, set(), nodes, set())
    maximum_clique = set()
    for clique in cliques:
        if len(clique) > len(maximum_clique):
            maximum_clique = clique
    return maximum_clique

def solution():
    g, nodes = parse_input()
    largest_clique = find_largest_clique(g, nodes)
    print(",".join(sorted(largest_clique)))

if __name__ == "__main__":
    solution()
