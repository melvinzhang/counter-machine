"""
An AST and interpreter for Portable Minsky Machine notation,
https://esolangs.org/wiki/Portable_Minsky_Machine_Notation

A program is a list of instructions.
A inc is just the register number.
while(dec) is a pair (register number, while_block)
if(dec) is a triple (register number, then_block, else_block)
"""

from collections import defaultdict

def size(prog):
    res = 0
    for instr in prog:
        if isinstance(instr, int):
            res += 1
        else:
            _, instrs = instr
            res += 1 + size(instrs)
    return res

def run(prog, n):
    r = defaultdict(int)
    r[0] = n
    sim(prog, r)
    return sum(r.values())

def sim(prog, r):
    for instr in prog:
        # inc instruction
        if isinstance(instr, int):
            c = instr
            r[c] += 1
        # while(dec)
        elif len(instr) == 2:
            c, while_block = instr
            while r[c] > 0:
                r[c] -= 1
                sim(while_block, r)
        # if(dec)
        elif len(instr) == 3:
            c, then_block, else_block = instr
            if r[c] > 0:
                r[c] -= 1
                sim(then_block, r)
            else:
                sim(else_block, r)
        else:
            assert False, "illegal instruction"

def check(n, res, expected):
    assert res == expected, (res, expected)
    print(n, res)
              
def main():
    n = 5
    
    """
    while dec(r, 0):
        inc(r, 1)
        inc(r, 1)
    """
    double = [(0, [1, 1])] 
    check(size(double), run(double, n), 2*n)

    """
    inc(r, 1)
    while dec(r, 0):
        while dec(r, 1):
            inc(r, 3)
            inc(r, 3)
        while dec(r, 3):
            inc(r, 1)
            inc(r, 1)
    """
    exp8 = [1, (0, [(1, [2, 2]), (2, [1, 1])])]
    check(size(exp8), run(exp8, n), 2**(2*n)) 

    exp10 = [1, (0, [(1, [2, 2, 2]), (2, [1, 1, 1])])]
    check(size(exp10), run(exp10, n), 3**(2*n)) 

    sum7 = [0, 0, 0, (0, [1, 1, 1])] 
    check(size(sum7), run(sum7, 0), 9)

if __name__ == "__main__":
    main()
