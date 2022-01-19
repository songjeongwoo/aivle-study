A=int(input())
B=int(input())
C=int(input())
D=str(A*B*C)
E=list(D)

for i in range(10):
    print(E.count(str(i)))