D = int(input())
C = int(input())

dias_min = (D * 180) / 20
ticket = dias_min * 12000

T = ticket // C
print(T)