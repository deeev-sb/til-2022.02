# 2019 KAKAO BLIND RECRUITMENT 실패율

def solution(N, stages):
    answer = []
    failure_rate = {}
    challenger = len(stages)
    
    for i in range(1, N+1): # 1단계부터 순서대로 확인
        if challenger != 0: # 도전자가 있으면
            count = stages.count(i)
            failure_rate[i] = count / challenger
            challenger -= count # count는 상위 스테이지에 도달 X
        else:
            failure_rate[i] = 0
    
    answer = sorted(failure_rate, key=lambda x : failure_rate[x], reverse=True)
    return answer
