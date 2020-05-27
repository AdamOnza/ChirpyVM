# ChirpyVM
A virtual machine created late at night while trying to write a tweet.
Version 0.01. 

Registers:
A, B General registers.
N true if negative flag register
ib instruction buffer (Holding instructions to be executed)

Memory is Python ints

Instructions (4 bit opcodes):
0 no-op ( Go to next word in memory.)
1 lit x (A=[pc]++ ; loads the next word in memory. incs pc)
2 inp
3 out
4 fetch A = [A]
5 store [A] = B
6 swap (A,B = B,A)
7 sub (A = A-B [B's end value is undefined ATM])
8 jn d (if N: pc = d)
9-14 reserved
15 halt (EG -1 is infinite halts)

A single word can contain multiple op-codes. If an instructions have rations, they are located is the following words
The opcodes are executed least to most significant. So that
[0x4321,
 5,
 6]
is functionally the same as
[1,5,
 2,
 3,
 4,6]
