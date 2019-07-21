# Implemention of Petersen's algorithm for multipling two numbers using a 3 counter machine
# input is stored in counter A and counter B, third counter used as scratch memory
# output is stored in counter B

# Correctness verified by testing all tuples (i,j) where 0 <= i,j < 100

def odd(n):
    return n % 2 == 1

def even(n):
    return n % 2 == 0

def div3(n):
    return n % 3 == 0

def div5(n):
    return n % 5 == 0

def mult1972(A, B):
    X, Y = A, B
    B = 2 * B + 1
    assert B == 2*Y + 1
    while A > 0:
        B = 2 * B
        A = A - 1
    assert B == 2**X * (2*Y + 1)
    A = 1
    while even(B):
        B = B // 2
        A = A * 2
    B = B // 2
    assert A == 2**X and B == Y
    while B > 0:
        A = A * 3
        B = B - 1
    assert A == 2**X * 3**Y and B == 0
    while even(A):
        A = A // 2
        while div3(A):
            A = A // 3
            A = A * 5
            B = B + 1
        while div5(A):
            A = A // 5
            A = A * 3
    return B

def mult2018(A, B):
    # special case: A * 0 = 0
    if B == 0: return 0

    # flag in lowest bit
    A = 2 * A + 1

    # loop 1
    while B > 0:
        A = 2 * A
        if odd(B): A = A + 1
        A = 2 * A
        B = B // 2
    B = A
    A = A + 1
    # loop 2
    while even(B):
        A = 2 * A
        B = B // 4
    B = B - 1
    # loop 3
    while even(A):
        B = 8 * B
        A = A // 2
    A = A - 1
    # loop 4
    while even(A):
        A = A // 2
        B = B // 4
        if odd(A): A = A + B
        A = A // 2
        B = B // 2
    A = A - B
    B = A
    B = B // 2
    
    return B

for i in range(100):
    for j in range(100):
        m2018 = mult2018(i,j)
        m1972 = mult1972(i,j)
        print(i, j, m2018)
        assert i * j == m2018 == m1972

print("All tests passed")

