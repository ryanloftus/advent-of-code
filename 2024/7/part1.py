with open("input.txt") as f:
    equations = f.read().split("\n")

# does lhs = acc ? rhs where ? is either * or +
def is_possible(lhs, rhs, acc):
    if len(rhs) == 0:
        return acc == lhs
    else:
        return is_possible(lhs, rhs[1:], acc + rhs[0]) or is_possible(lhs, rhs[1:], acc * rhs[0])

test_val_sum = 0
for eq in equations:
    eq_parts = eq.split(": ")
    lhs = int(eq_parts[0])
    rhs = [int(x) for x in eq_parts[1].split(" ")]
    if is_possible(lhs, rhs[1:], rhs[0]):
        test_val_sum += lhs
print(test_val_sum)
