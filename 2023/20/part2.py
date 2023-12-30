from queue import Queue, PriorityQueue
from math import lcm

file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

LOW_PULSE = 0
HIGH_PULSE = 1

modules = dict()
for line in lines:
    split_line = line.split(" -> ")
    destinations = split_line[1].split(", ")
    if split_line[0][0] == "b":
        modules[split_line[0]] = (destinations, "b", None)
    elif split_line[0][0] == "%":
        modules[split_line[0][1:]] = (destinations, "%", False)
    else:
        modules[split_line[0][1:]] = (destinations, "&", None)

for k in modules.keys():
    v = modules[k]
    if v[1] == "&":
        inputs = dict()
        for kp, vp in modules.items():
            destinations = vp[0]
            if k in destinations:
                inputs[kp] = LOW_PULSE
        modules[k] = (v[0], v[1], inputs)


def all_inputs_are_high(inputs):
    for _, pulse in inputs.items():
        if pulse == LOW_PULSE:
            return False
    return True


def send_pulses(q, src, pulse, destinations):
    for dest in destinations:
        q.put((src, dest, pulse))

hj_inputs = dict()
hj_cycles = []

def press_button(i):
    q = Queue()
    q.put((None, "broadcaster", LOW_PULSE))

    while not q.empty():
        src, node, pulse = q.get()
        if node not in modules:
            continue
        destinations, typ, data = modules[node]
        if typ == "b":
            send_pulses(q, node, pulse, destinations)
        elif typ == "%" and pulse == LOW_PULSE:
            new_pulse = LOW_PULSE if data else HIGH_PULSE
            send_pulses(q, node, new_pulse, destinations)
            modules[node] = (destinations, typ, not data)
        elif typ == "&":
            data[src] = pulse
            if node == "hj" and pulse == HIGH_PULSE:
                if src in hj_inputs:
                    start = hj_inputs[src]
                    length = i - start
                    hj_cycles.append((start, length))
                else:
                    hj_inputs[src] = i
            new_pulse = LOW_PULSE if all_inputs_are_high(data) else HIGH_PULSE
            send_pulses(q, node, new_pulse, destinations)

# rx only receives input from hj, hj is conjunctive. We can find patterns in hj's inputs to see when they are high.
# by printing each time an input to hj sends a high pulse, we know that they follow cycles
# we also know that each cycle only repeats once in the first 10000 button presses
for i in range(10000):
    press_button(i)

# outputs: [(3888, 3889), (3910, 3911), (3946, 3947), (4012, 4013)]
print(hj_cycles)

print(lcm(3889, 3911, 3947, 4013))
