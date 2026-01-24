from queue import Queue

class Machine:
    def __init__(self, lights, buttons, joltage):
        self.lights = lights
        self.buttons = buttons
        self.joltage = joltage

    def matches(self, state):
        for i in range(len(self.lights)):
            if state[i] != self.lights[i]:
                return False
        return True

def parse_line(l):
    lights = [c == '#' for c in l.split(']')[0][1:]]
    buttons = [[int(i.strip(') ')) for i in button.split(',')] for button in l.split(']')[1].split('{')[0].split('(')[1:]]
    joltage = [int(j) for j in l.split('{')[1].strip('}').split(',')]
    return Machine(lights, buttons, joltage)

def parse_input():
    with open("input.txt") as f:
        return [parse_line(l.strip('\n')) for l in f]
    
def get_new_state(s, b):
    new = [s[i] for i in range(len(s))]
    for i in b:
        new[i] = not new[i]
    return new

def min_presses(machine):
    q = Queue()
    q.put_nowait(([False] * len(machine.lights), 0))
    while not q.empty():
        state, presses = q.get_nowait()
        if machine.matches(state):
            return presses
        for b in machine.buttons:
            new_state = get_new_state(state, b)
            q.put_nowait((new_state, presses + 1))

def solution():
    machines = parse_input()
    min_total_presses = 0
    for machine in machines:
        min_total_presses += min_presses(machine)
    print(min_total_presses)

if __name__ == "__main__":
    solution()
