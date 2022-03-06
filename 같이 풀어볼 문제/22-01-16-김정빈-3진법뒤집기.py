#프로그래머스/월간코드챌린지시즌1/3진법뒤집기
def solution(n):
    li=[]
    ans=0
    answer=0
    while n>0:
        n,ans=divmod(n,3)
        li.append(ans)
    li=list(map(str,li))
    a=''.join(li)
    answer=int(a,3)
    return answer