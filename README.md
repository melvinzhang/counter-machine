Counter Machine
===============

A k counter machine has k counters, each able to store a single natural number.
Initialy all counters are zero. For problems with inputs, some of the counters
are used to store the input.

The possible instructions are
1) increment counter i, jump to line n
2) decrement counter i, if successful jump to line n else jump to line m

Multiplication with 3CM
-----------------------

A 3CM with X in counter 1 and Y in counter 2 is able to compute X * Y in counter 2.

Proof: Two algorithms are given in [mult.py](mult.py), one from schroeppel1972 and the other from petersen2018


Squaring with 3CM
-----------------

A 3CM with X in counter 1 is able to compute X^2.

Proof: See [square.py](square.py) for the algorithm from schroeppel1972
