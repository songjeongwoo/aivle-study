# 11022. A+B -8
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

t = int(sys.stdin.readline())
for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #{}: {} + {} = {}'.format(i, a, b, a+b))