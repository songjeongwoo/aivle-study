# 10950. A+B -3
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

a = int(input())

for i in range(a):
    x, y = map(int, input().split())
    print(x+y)