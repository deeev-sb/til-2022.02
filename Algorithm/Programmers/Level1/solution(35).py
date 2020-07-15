# 예산
# Summer/Winter Coding(~2018)

def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in range(len(d)):
        if budget >= d[i]:
            budget -= d[i]
            answer += 1
    return answer
