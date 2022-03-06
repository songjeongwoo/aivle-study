# 풀이1
def solution(numbers):
    sum = 45
    for i in numbers:
        sum -= i
    return sum

# 풀이2
def solution(numbers):
    return 45 - sum([i for i in numbers])