def parse_input():
    with open("input.txt") as f:
        code = f.read().replace("\n", ": ").split(": ")
        return int(code[1]), int(code[3]), int(code[5]), [int(x) for x in code[8].split(",")]

def get_combo_value(a, b, c, combo_operand):
    if combo_operand >= 0 and combo_operand <= 3:
        return combo_operand
    if combo_operand == 4:
        return a
    if combo_operand == 5:
        return b
    if combo_operand == 6:
        return c

def run_code(a, b, c, code):
    pc = 0
    output = []
    while pc < len(code):
        combo_val = get_combo_value(a, b, c, code[pc+1])
        if code[pc] == 0:
            a = a // (2 ** combo_val)
        elif code[pc] == 1:
            b = b ^ code[pc+1]
        elif code[pc] == 2:
            b = combo_val % 8
        elif code[pc] == 3:
            if a != 0:
                pc = code[pc+1]
                continue
        elif code[pc] == 4:
            b = b ^ c
        elif code[pc] == 5:
            output.append(combo_val % 8)
        elif code[pc] == 6:
            b = a // (2 ** combo_val)
        elif code[pc] == 7:
            c = a // (2 ** combo_val)
        pc += 2

    return output


def solution():
    a, b, c, code = parse_input()
    output = run_code(a, b, c, code)
    print(",".join(str(x) for x in output))

if __name__ == "__main__":
    solution()
