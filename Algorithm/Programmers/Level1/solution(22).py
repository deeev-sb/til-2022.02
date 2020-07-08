# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    n = str(n)
    for i in range(1,len(n)):
        answer.append(int(n[-i]))
    answer.append(int(n[0]))
    return answer
