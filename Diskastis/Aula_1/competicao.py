# x = (a + b + (|a - b|)) / 2.

# x = (a + b + abs(a - b))/2

A = int(input())
L = int(input())
P = int(input())
H = int(input())

AL = (A + L + abs(A - L))/2
ALP = (AL + P + abs(AL - P))/2
ALPH = ALP*H

print(int(ALPH))