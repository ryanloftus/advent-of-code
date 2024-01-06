from random import randint
from queue import Queue
from collections import defaultdict

file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

class Edge:
    def __init__(self, s, t):
        self.s = s
        self.t = t
        self.cap = 1
        self.flow = 0

def add_edge_if_not_present(g, n1, n2):
    for e in g[n1]:
        if e.t == n2:
            return
    fwd = Edge(n1, n2)
    rev = Edge(n2, n1)
    fwd.rev = rev
    rev.rev = fwd
    g[n1].append(fwd)
    g[n2].append(rev)

def build_graph():
    g = dict()
    for line in lines:
        part = line.partition(": ")
        src = part[0]
        if src not in g:
            g[src] = []
        for dest in part[2].split(" "):
            if dest not in g:
                g[dest] = []
            add_edge_if_not_present(g, src, dest)
    return g

# max-flow, min-cut problem?
# if there's three wires that can be cut, then that means 3 is an s-t cut for some s-t that we don't actually know, we could try guessing s-t though
# if we assume that neither of the two groups is very small, we shouldn't need many guesses
# the approach would be:
# 1. guess s-t
# 2. find s-t min-cut with FordFulkerson
# 3. if min-cut has size 3, find group sizes and print the product, otherwise, go back to 1.

def min_cut(g, s, t):
    flow = 0
    done = False
    while not done:
        q = Queue()
        q.put_nowait(s)
        pred = defaultdict(lambda: None)
        while not q.empty() and pred[t] == None:
            cur = q.get_nowait()
            for e in g[cur]:
                if pred[e.t] == None and e.t != s and e.cap > e.flow:
                    pred[e.t] = e
                    q.put_nowait(e.t)

        if pred[t] != None:
            df = 1
            e = pred[t]
            while e != None:
                e.flow = e.flow + df
                e.rev.flow = e.rev.flow - df
                e = pred[e.s]
            flow += df
        else:
            done = True
    return flow, g

def bfs(g, s):
    q = Queue()
    q.put_nowait(s)
    v = set()
    v.add(s)
    while not q.empty():
        node = q.get_nowait()
        for e in g[node]:
            if e.cap > e.flow and e.t not in v:
                q.put_nowait(e.t)
                v.add(e.t)
    return len(v)

while True:
    g = build_graph()
    nodes = list(g.keys())
    s = randint(0, len(nodes) - 1)
    t = randint(0, len(nodes) - 1)
    while s == t:
        t = randint(0, len(nodes) - 1)
    s = nodes[s]
    t = nodes[t]

    cut_size, gr = min_cut(g, s, t)
    if cut_size == 3:
        s_group_size = bfs(gr, s)
        t_group_size = len(nodes) - s_group_size
        print(s_group_size * t_group_size)
        break
