class Button:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

class Machine:
    def __init__(self, button_a, button_b, price_x, price_y):
        self.a = button_a
        self.b = button_b
        self.px = price_x
        self.py = price_y

def line_to_button(line):
    b = [int(s.strip(",XY+")) for s in line.split(" ")[2:]]
    return Button(b[0], b[1])

def line_to_prize(line):
    b = [int(s.strip(",XY=")) for s in line.split(" ")[1:]]
    return b[0], b[1]

def min_tokens_to_beat(machine: Machine):
    min_tokens = 1000
    for ap in range(101):
        for bp in range(101):
            if ap * machine.a.dx + bp * machine.b.dx == machine.px and \
               ap * machine.a.dy + bp * machine.b.dy == machine.py:
                min_tokens = min(min_tokens, 3 * ap + bp)
    return None if min_tokens == 1000 else min_tokens

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
