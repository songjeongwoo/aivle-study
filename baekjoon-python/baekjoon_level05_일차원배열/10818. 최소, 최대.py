# 10818. 최소, 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

import sys

a = sys.stdin.readline()
b = list(map(int, sys.stdin.readline().split()))

print(min(b), max(b))