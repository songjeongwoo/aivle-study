#프로그래머스/월간코드챌린지시즌1/내적
def solution(a,b):
    answer=0
    for i in range(len(b)):
        answer+=(a[i]*b[i])
    return answer