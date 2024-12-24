import numpy as np
import math

OFFSET = 10000000000000

class Button:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

class Machine:
    def __init__(self, button_a, button_b, price_x, price_y):
        self.a = button_a
        self.b = button_b
        self.px = price_x + OFFSET
        self.py = price_y + OFFSET

def line_to_button(line):
    b = [int(s.strip(",XY+")) for s in line.split(" ")[2:]]
    return Button(b[0], b[1])

def line_to_prize(line):
    b = [int(s.strip(",XY=")) for s in line.split(" ")[1:]]
    return b[0], b[1]

def is_valid(M, s, c):
    return (np.matmul(M, s) == c).all()

def min_tokens_to_beat(machine: Machine):
    """
    ap * adx + bp * bdx = px
    ap * ady + bp * bdy = py
    """
    adx = machine.a.dx
    ady = machine.a.dy
    bdx = machine.b.dx
    bdy = machine.b.dy

    M = [[adx, bdx], [ady, bdy]]
    c = [machine.px, machine.py]

    if np.linalg.det(M) == 0:
        raise "Singular matrix found"

    s = np.linalg.solve(M, c)
    sint = [int(np.round(x)) for x in s]
    if is_valid(M, sint, c):
        return 3 * sint[0] + sint[1]
    
    return None

with open("input.txt") as f:
    lines = f.read().split("\n")

machines = []
for i in range(0, len(lines), 4):
    a = line_to_button(lines[i])
    b = line_to_button(lines[i+1])
    px, py = line_to_prize(lines[i+2])
    machines.append(Machine(a, b, px, py))

tokens_used = 0
for machine in machines:
    tokens_to_beat = min_tokens_to_beat(machine)
    if tokens_to_beat is not None:
        tokens_used += tokens_to_beat
print(tokens_used)
