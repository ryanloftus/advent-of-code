from scipy.optimize import linprog

class Machine:
    def __init__(self, buttons, joltage):
        self.buttons = buttons
        self.joltage = joltage

def parse_line(l):
    buttons = [[int(i.strip(') ')) for i in button.split(',')] for button in l.split(']')[1].split('{')[0].split('(')[1:]]
    joltage = [int(j) for j in l.split('{')[1].strip('}').split(',')]
    return Machine(buttons, joltage)

def parse_input():
    with open("input.txt") as f:
        return [parse_line(l.strip('\n')) for l in f]

def min_presses(machine):
    A = [[0 for i in range(len(machine.buttons))] for j in range(len(machine.joltage))]
    for i in range(len(machine.buttons)):
        for j in machine.buttons[i]:
            A[j][i] = 1
    c = [1] * len(machine.buttons)
    bounds = [(0,1000) for i in range(len(machine.buttons))]
    return linprog(c=c, A_eq=A, b_eq=machine.joltage, bounds=bounds, integrality=c).fun

def solution():
    machines = parse_input()
    min_total_presses = 0
    for machine in machines:
        min_total_presses += min_presses(machine)
    print(min_total_presses)

if __name__ == "__main__":
    solution()
