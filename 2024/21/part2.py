from heapq import *

DPAD_BUTTONS = ["A", ">", "v", "<", "^"]

# maps from state to dictionary of (controller_button_pressed -> new_state)
DPAD_ADJ = {
    "A": {
        "v": ">",
        "<": "^",
        "A": "A"
    },
    ">": {
        "^": "A",
        "<": "v",
        "A": ">"
    },
    "v": {
        "^": "^",
        ">": ">",
        "<": "<",
        "A": "v"
    },
    "<": {
        ">": "v",
        "A": "<"
    },
    "^": {
        ">": "A",
        "v": "v",
        "A": "^"
    }
}

NUMPAD_ADJ = {
    "7": {
        ">": "8",
        "v": "4",
        "A": "7"
    },
    "8": {
        "<": "7",
        ">": "9",
        "v": "5",
        "A": "8"
    },
    "9": {
        "<": "8",
        "v": "6",
        "A": "9"
    },
    "4": {
        "^": "7",
        ">": "5",
        "v": "1",
        "A": "4"
    },
    "5": {
        "<": "4",
        "^": "8",
        ">": "6",
        "v": "2",
        "A": "5"
    },
    "6": {
        "<": "5",
        "^": "9",
        "v": "3",
        "A": "6"
    },
    "1": {
        ">": "2",
        "^": "4",
        "A": "1"
    },
    "2": {
        "<": "1",
        ">": "3",
        "^": "5",
        "v": "0",
        "A": "2"
    },
    "3": {
        "<": "2",
        "v": "A",
        "^": "6",
        "A": "3"
    },
    "0": {
        ">": "A",
        "^": "2",
        "A": "0"
    },
    "A": {
        "^": "3",
        "<": "0",
        "A": "A"
    }
}

NUMPAD_BUTTONS = ["A", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def parse_input():
    with open("input.txt") as f:
        return f.read().splitlines()

def update_state(state, controller_button, controller_costs, controllee_adj):
    pathlen, entered, controller_state, controllee_state = state

    if controller_button not in controllee_adj[controllee_state]:
        return None

    new_controllee_state = controllee_adj[controllee_state][controller_button]

    if controller_button == "A":
        entered += controllee_state

    return (pathlen+controller_costs[controller_state][controller_button], entered, controller_button, new_controllee_state)

def cost_for_controllee_to_press_button(controllee_target_button, initial_controllee_state, controller_costs, controllee_adj):
    q = [(0, "", "A", initial_controllee_state)]
    visited = set()
    while q:
        state = heappop(q)
        pathlen, entered, controller_state, controllee_state = state

        if entered == controllee_target_button:
            return pathlen

        if len(entered) > 0:
            continue

        if state in visited:
            continue
        visited.add(state)

        for button in DPAD_BUTTONS:
            new_state = update_state(state, button, controller_costs, controllee_adj)
            if new_state is not None:
                heappush(q, new_state)

def get_numpad_costs():
    cost = { state: { button: 1 for button in DPAD_BUTTONS } for state in DPAD_BUTTONS }
    for i in range(25):
        new_cost = { state: {} for state in DPAD_BUTTONS }
        for initial_controllee_state in DPAD_BUTTONS:
            for controllee_target_button in DPAD_BUTTONS:
                new_cost[initial_controllee_state][controllee_target_button] = cost_for_controllee_to_press_button(controllee_target_button, initial_controllee_state, cost, DPAD_ADJ)
        cost = new_cost
        
    numpad_cost = { state: {} for state in NUMPAD_BUTTONS }
    for initial_numpad_state in NUMPAD_BUTTONS:
        for numpad_target_button in NUMPAD_BUTTONS:
            numpad_cost[initial_numpad_state][numpad_target_button] = cost_for_controllee_to_press_button(numpad_target_button, initial_numpad_state, cost, NUMPAD_ADJ)
    return numpad_cost

def get_total_complexity(codes, costs):
    total_complexity = 0
    state = "A"
    for code in codes:
        complexity = 0
        for i in range(len(code)):
            complexity += costs[state][code[i]]
            state = code[i]
        complexity *= int(code[:3])
        total_complexity += complexity
    return total_complexity

def solution():
    """
    Idea:
    incrementally determine the cost of pressing a button on the next robots controller from each possible state.
    """
    codes = parse_input()
    costs = get_numpad_costs()
    complexity = get_total_complexity(codes, costs)
    print(complexity)

if __name__ == "__main__":
    solution()
