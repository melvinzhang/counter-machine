from collections import defaultdict

# using https://esolangs.org/wiki/Portable_Minsky_Machine_Notation

def dec(r, i):
    if r[i] > 0:
        r[i] -= 1
        return True
    else:
        return False

def inc(r, i):
    r[i] += 1
    return True

def sim(f, n):
    r = defaultdict(int)
    r[0] = n
    f(r)
    return sum(r.values())

def check(n, res, expected):
    assert res == expected, (res, expected)
    print(n, res)

# conjecture: 2n is optimal for 3 instructions
def double(r):
    while dec(r, 0):
        inc(r, 1)
        inc(r, 1)

def add(r):
    inc(r, 0)
    inc(r, 0)
    inc(r, 0)

# 2n+2 possible for 4 instructions
def incdouble(r):
    inc(r, 0)
    double(r)

# conjecture: 3n is optimal for 4 instructions
def triple(r):
    while dec(r, 0):
        inc(r, 1)
        inc(r, 1)
        inc(r, 1)

def double_self(r, n):
    while dec(r, n):
        inc(r, 3)
        inc(r, 3)
    while dec(r, 3):
        inc(r, n)

# computes n*2^n using 9 instructions
def exp9(r):
    while dec(r, 0):
        inc(r, 1)
        inc(r, 2)
    while dec(r, 1):
        double_self(r, 2)

# computes n*2^(2n) using 10 instructions
# not optimal!
def exp10(r):
    while dec(r, 0):
        inc(r, 1)
        inc(r, 2)
    while dec(r, 2):
        while dec(r, 1):
            inc(r, 3)
            inc(r, 3)
        while dec(r, 3):
            inc(r, 1)
            inc(r, 1)

# computes 2^(4n) using 11 instructions
def exp11(r):
    inc(r, 1)
    while dec(r, 0):
        inc(r, 2)
        inc(r, 2)
    while dec(r, 2):
        while dec(r, 1):
            inc(r, 3)
            inc(r, 3)
        while dec(r, 3):
            inc(r, 1)
            inc(r, 1)

# computes 2^n using 7 instructions
def exp7(r):
    inc(r, 1)
    while dec(r, 0):
        while dec(r, 1):
            inc(r, 3)
            inc(r, 3)
        while dec(r, 3):
            inc(r, 1)

# computes 2^(2n) using 8 instructions
def exp8(r):
    inc(r, 1)
    while dec(r, 0):
        while dec(r, 1):
            inc(r, 3)
            inc(r, 3)
        while dec(r, 3):
            inc(r, 1)
            inc(r, 1)

def exp9b(r):
    inc(r, 1)
    exp8(r)

def exp9c(r):
    inc(r, 1)
    while dec(r, 0):
        while dec(r, 1):
            inc(r, 3)
            inc(r, 3)
            inc(r, 3)
        while dec(r, 3):
            inc(r, 1)
            inc(r, 1)

# computes 3*(2n)
def exp10b(r):
    inc(r, 1)
    while dec(r, 0):
        while dec(r, 1):
            inc(r, 3)
            inc(r, 3)
            inc(r, 3)
        while dec(r, 3):
            inc(r, 1)
            inc(r, 1)
            inc(r, 1)

# 7 instructions that output 9, more efficient that using all inc
def sum7(r):
    inc(r, 0)
    inc(r, 0)
    inc(r, 0)
    while dec(r, 0):
        inc(r, 1)
        inc(r, 1)
        inc(r, 1)

n = 0
print(f"--- largest sum ---")
check(7, sim(sum7, n), 9)

n = 5
print(f"--- largest function (n = {n}) ---")
check(3, sim(add, n), n+3)
check(3, sim(double, n), 2*n)

check(4, sim(incdouble, n), 2*(n+1))
check(4, sim(triple, n), 3*n)

check(7, sim(exp7, n), 2**n)
check(8, sim(exp8, n), 2**(2*n))
check(9, sim(exp9, n), n*2**n)
check(9, sim(exp9b, n), 2**(2*n+1))
check(9, sim(exp9c, n), 2**n * 3**n)
check(10, sim(exp10, n), n*4**n)
check(10, sim(exp10b, n), 3**(2*n))
check(11, sim(exp11, n), 2**(4*n))
