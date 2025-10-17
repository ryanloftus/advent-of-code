def parse_input():
    wire_values = dict()
    gate_connections = dict()
    with open("input.txt") as f:
        for line in f:
            sline = line.strip()
            if sline == "":
                continue
            if ":" in sline:
                parsed = sline.split(": ")
                if parsed[1] == "0":
                    wire_values[parsed[0]] = False
                else:
                    wire_values[parsed[0]] = True
            else:
                parsed = sline.split(" ")
                gate_connections[parsed[-1]] = tuple(parsed[:3])
    return wire_values, gate_connections

def perform_op(op, lhs, rhs):
    if op == "AND":
        return lhs and rhs
    if op == "OR":
        return lhs or rhs
    if op == "XOR":
        return lhs ^ rhs

def get_wire_value(gates, wire_values, target_wire):
    if target_wire in wire_values:
        return wire_values[target_wire]
    lhs, op, rhs = gates[target_wire]
    lhs_value = get_wire_value(gates, wire_values, lhs)
    rhs_value = get_wire_value(gates, wire_values, rhs)
    wire_value = perform_op(op, lhs_value, rhs_value)
    wire_values[target_wire] = wire_value
    return wire_value

def solution():
    wire_values, gates = parse_input()
    z_wires = sorted(filter(lambda x: x.startswith("z"), gates.keys()))
    answer = 0
    for i in range(len(z_wires)):
        answer += get_wire_value(gates, wire_values, z_wires[i]) << i
    print(answer)

if __name__ == "__main__":
    solution()
