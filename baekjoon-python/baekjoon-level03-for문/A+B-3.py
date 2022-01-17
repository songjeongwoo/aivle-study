for _ in range(int(input())):
    print(sum(map(int, input().split())))

T = int(input())
for i in range(T):
    A,B = map(int, input().split())
    print(A+B)