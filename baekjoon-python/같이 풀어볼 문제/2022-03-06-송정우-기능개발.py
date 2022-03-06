from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    tmp = []
    
    while progresses:
        cnt = 0
        if progresses[0] >= 100:
            for _ in range(len(progresses)):
                if progresses[0] >= 100:
                    progresses.popleft()
                    speeds.popleft()
                    cnt+=1
                else:
                    break
        else:
            for j in range(100):
                if j < len(progresses):
                    progresses[j] += speeds[j]
        tmp.append(cnt)
        
    return [n for n in tmp if n != 0]