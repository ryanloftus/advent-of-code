def check_code(a, desired_output):
    output_idx = 0
    while a > 0:
        lowa = a & 0b111
        x = lowa ^ 0b111
        b = x ^ ((a >> x) & 0b111) ^ 0b100
        if b != desired_output[output_idx]:
            return False
        output_idx += 1
        a //= 8
    return True

def iterate(a, desired_output, iter):
    if iter == -1:
        return a
    
    for lowa in range(8):
        an = a * 8 + lowa
        x = lowa ^ 0b111
        out = x ^ ((an >> x) & 0b111) ^ 0b100
        if out == desired_output[iter]:
            ans = iterate(an, desired_output, iter-1)
            if ans != None:
                return ans

    return None

def solution():
    """
    Idea:
    - there is one output per iteration of the code
    - the code iterates until a is 0
    - each iteration divides a by 8
    - each output corresponds to 3-bits of a
    - we can determine a 3-bits-at-a-time by iterating backwards through the list of outputs
    """
    desired_output = [2,4,1,7,7,5,4,1,1,4,5,5,0,3,3,0]
    a = iterate(0, desired_output, len(desired_output) - 1)
    print(a)
    print(check_code(a, desired_output))

if __name__ == "__main__":
    solution()
