def solution(absolutes, signs):
    ans=[]
    for i in range(len(absolutes)):
        if signs[i] == False:
            a = absolutes[i]*(-1)
        else:
            a = absolutes[i]
        ans.append(a)
        answer= sum(ans)
    return answer