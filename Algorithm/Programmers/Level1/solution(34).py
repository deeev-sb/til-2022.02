# 체육복

def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in range(len(lost)):
        if lost[i] in reserve:
            answer += 1
            reserve.remove(lost[i])
            lost[i] = 0
    
    if 0 in lost:
        lost.remove(0)
    
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]-1 or lost[i] == reserve[j]+1:
                answer += 1
                lost[i], reserve[j] = -10, -10
    
    return answer
