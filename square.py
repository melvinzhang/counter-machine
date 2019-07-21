# Implemention of Schroeppel's algorithm for squaring a number using a 3 counter machine
# Trick is to use the fact that N^2 = 1 + 3 + ... + (2N - 3) + (2N - 1)

def square1972(A):
    B = 0
    C = 0
    while A > 0:
        A = A - 1
        while A > 0:
            A = A - 1
            C = C + 2
            B = B + 1
        C = C + 1
        while B > 0:
            B = B - 1
            A = A + 1
    return C

for i in range(100):
    sq = square1972(i)
    print(i, sq)
    assert i * i == sq

print("All tests passed")

