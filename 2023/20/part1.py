from queue import Queue

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
    return (0, len(destinations)) if pulse == HIGH_PULSE else (len(destinations), 0)

def press_button():
    low = 1
    high = 0
    q = Queue()
    q.put((None, "broadcaster", LOW_PULSE))

    while not q.empty():
        src, node, pulse = q.get()
        if node not in modules:
            continue
        destinations, typ, data = modules[node]
        if typ == "b":
            l, h = send_pulses(q, node, pulse, destinations)
            low += l
            high += h
        elif typ == "%" and pulse == LOW_PULSE:
            new_pulse = LOW_PULSE if data else HIGH_PULSE
            l, h = send_pulses(q, node, new_pulse, destinations)
            low += l
            high += h
            modules[node] = (destinations, typ, not data)
        elif typ == "&":
            data[src] = pulse
            new_pulse = LOW_PULSE if all_inputs_are_high(data) else HIGH_PULSE
            l, h = send_pulses(q, node, new_pulse, destinations)
            low += l
            high += h

    return low, high

total_low_pulses = 0
total_high_pulses = 0

for i in range(1000):
    low, high = press_button()
    total_high_pulses += high
    total_low_pulses += low

print(total_high_pulses * total_low_pulses)
