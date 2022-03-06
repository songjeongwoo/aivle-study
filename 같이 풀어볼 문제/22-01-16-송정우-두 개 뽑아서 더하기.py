def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    answer = list(set(answer))
    answer.sort()
    
    return answer

'''
다른 사람 풀이:

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
'''
