def solution(n, lost, reserve):
    re = list(set(reserve) - set(lost))                # 도난당하지 않은 여유분 있는 학생
    lo = list(set(lost) - (set(reserve) - set(re)))    # 정말 빌려야 하는 학생
    answer = n-len(lo)                                 # 체육복을 빌리지 않아도 되는 학생 수
    
    for i in re:
        for j in lo:
            if (i-1 == j) or (i+1==j):
                lo.remove(j)
                answer += 1
    return answer