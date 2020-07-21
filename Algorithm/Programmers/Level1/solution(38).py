# 2018 KAKAO BLIND RECRUITMENT [1차] 다트 게임

def solution(dartResult):
    answer = 0
    temp = 0
    temp_pre = 0
    num = '0123456789'
    count = 0
    for i in range(len(dartResult)):
        print(count, temp)
        if count == len(dartResult):
            break
        if dartResult[count] in num:
            answer += temp
            temp_pre = temp
            if dartResult[count+1] == '0':
                count += 1
                temp = 10
            else:
                temp = int(dartResult[count])
        elif dartResult[count] == 'D':
            temp = temp**2
        elif dartResult[count] == 'T':
            temp = temp**3
        elif dartResult[count] == '*':
            answer += temp_pre
            temp *= 2
        elif dartResult[count] == '#':
            temp = -temp
        count += 1
    answer += temp
    return answer