def get_op_tuple(a):
    if a[0] < a[2]:
        return (a[0], a[1], a[2])
    else:
        return (a[2], a[1], a[0])

def parse_input():
    wire_values = dict()
    gate_connections = dict()
    reverse_gates = dict()
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
                gate_op = get_op_tuple(parsed[:3])
                gate_connections[parsed[-1]] = gate_op
                reverse_gates[gate_op] = parsed[-1]
    return wire_values, gate_connections, reverse_gates

def get_wire_name(c, n):
    if n < 10:
        return c + "0" + str(n)
    return c + str(n)

def swap_wires(gates, reverse_gates, w1, w2):
    gate1 = gates[w1]
    gate2 = gates[w2]
    reverse_gates[gate1] = w2
    reverse_gates[gate2] = w1
    gates[w1] = gate2
    gates[w2] = gate1

def find_swap_targets(gates, lhs, op, rhs, target):
    for wire in gates.keys():
        if wire == target:
            candidate_lhs, candidate_op, candidate_rhs = gates[wire]
            if candidate_op != op:
                continue
            if lhs == candidate_lhs:
                return rhs, candidate_rhs
            if lhs == candidate_rhs:
                return rhs, candidate_lhs
            if rhs == candidate_rhs:
                return lhs, candidate_lhs
            if rhs == candidate_lhs:
                return lhs, candidate_rhs

def find_swaps(gates, wire_values, reverse_gates):
    swapped = []
    carry = "jfb"
    for i in range(1, 45):
        xin = get_wire_name("x", i)
        yin = get_wire_name("y", i)
        zout = get_wire_name("z", i)

        bitsum_wire = reverse_gates[(xin, "XOR", yin)]

        result_wire = get_op_tuple([carry, "XOR", bitsum_wire])
        if gates[zout] != result_wire:
            swap_wire1 = None
            swap_wire2 = None
            if result_wire in reverse_gates:
                swap_wire1 = reverse_gates[result_wire]
                swap_wire2 = zout
            else:
                swap_wire1, swap_wire2 = find_swap_targets(gates, carry, "XOR", bitsum_wire, zout)
                if swap_wire1 == bitsum_wire:
                    bitsum_wire = swap_wire2
                else:
                    carry = swap_wire2
            print("swap", swap_wire1, swap_wire2)
            swap_wires(gates, reverse_gates, swap_wire1, swap_wire2)
            swapped += [swap_wire1, swap_wire2]

        # find next carry wire
        carry1 = reverse_gates[get_op_tuple([bitsum_wire, "AND", carry])]
        carry2 = reverse_gates[(xin, "AND", yin)]
        carry = reverse_gates[get_op_tuple([carry1, "OR", carry2])]
    return sorted(swapped)

def solution():
    """
    Idea:
    The general formula for a z wire should be:
    ((y01 AND x01) OR ((y00 AND x00) AND (y01 XOR x01))) XOR (x02 XOR y02) -> z02

    notice that:
    carry = ((y01 AND x01) OR ((y00 AND x00) AND (y01 XOR x01)))

    if we reach a gate that breaks this pattern, look for a swap that fixes the pattern
    """

    wire_values, gates, reverse_gates = parse_input()
    swapped_gates = find_swaps(gates, wire_values, reverse_gates)
    print(",".join(swapped_gates))

if __name__ == "__main__":
    solution()
