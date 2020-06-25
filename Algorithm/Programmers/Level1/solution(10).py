# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = "김서방은 %d에 있다" %(i)
    return answer