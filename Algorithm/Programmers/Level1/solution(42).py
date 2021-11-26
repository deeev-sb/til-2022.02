# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    numCheck = [0] * 10
    
    for n in numbers :
        numCheck[n] = 1
    
    for i in range(10) :
        if (numCheck[i] == 0) :
            answer += i
    
    return answer