def solution(n):
    answer = ''
    r = 0
    tmp = []
    
    while n > 0:
        n, r = divmod(n, 3)
        tmp.append(r)
    
    for i in tmp:
        answer += str(i)
    
    return int(answer, 3)

'''
다른 사람 코드:

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

'''