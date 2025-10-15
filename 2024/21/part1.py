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

def parse_input():
    with open("input.txt") as f:
        return f.read().splitlines()
    
def update_state(state, button):
    pathlen, entered, robot_1_state, robot_2_state, robot_3_state = state
    
    if button not in DPAD_ADJ[robot_1_state]:
        return None

    new_robot_1_state = DPAD_ADJ[robot_1_state][button]

    if button != "A":
        return (pathlen+1, entered, new_robot_1_state, robot_2_state, robot_3_state)
    
    if robot_1_state not in DPAD_ADJ[robot_2_state]:
        return None
    
    new_robot_2_state = DPAD_ADJ[robot_2_state][robot_1_state]

    if robot_1_state != "A":
        return (pathlen+1, entered, new_robot_1_state, new_robot_2_state, robot_3_state)
    
    if robot_2_state not in NUMPAD_ADJ[robot_3_state]:
        return None
    
    new_robot_3_state = NUMPAD_ADJ[robot_3_state][robot_2_state]

    if robot_2_state == "A":
        entered += robot_3_state

    return (pathlen+1, entered, new_robot_1_state, new_robot_2_state, new_robot_3_state)

def shortest_sequence(code):
    q = [(0, "", "A", "A", "A")]
    visited = set()
    while q:
        state = heappop(q)
        pathlen, entered, robot_1_state, robot_2_state, robot_3_state = state

        if entered == code:
            return pathlen
        
        if entered != code[:len(entered)]:
            continue

        if state in visited:
            continue
        visited.add(state)

        for button in DPAD_BUTTONS:
            new_state = update_state(state, button)
            if new_state is not None:
                heappush(q, new_state)


def solution():
    codes = parse_input()
    total_complexity = 0
    for code in codes:
        complexity = int(code[:3]) * shortest_sequence(code)
        total_complexity += complexity
    print(total_complexity)

if __name__ == "__main__":
    solution()
