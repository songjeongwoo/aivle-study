from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    tmp = []
    
    while progresses:
        cnt = 0
        if progresses[0] >= 100:  # 첫번째가 100이상이면
            for _ in range(len(progresses)):  # 전체 중 100이상인 개수 카운트
                if progresses[0] >= 100:
                    progresses.popleft()
                    speeds.popleft()
                    cnt+=1
                else:
                    break
        else:  # 첫번째가 100미만이면 전체 과정에 speed 더하기
            for j in range(100):
                if j < len(progresses):
                    progresses[j] += speeds[j]
        tmp.append(cnt)
        
    return [n for n in tmp if n != 0]