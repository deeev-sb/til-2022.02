# 소수 찾기

def solution(n):
    answer = 0
    if n >= 2 :
        answer += 1
        for i in range(3, n+1, 2): # 짝수 제외
            check = True
            if (int(i**0.5))**2 == n: # 제곱근 제외
                check = False
            else :
                for j in range(3, int(i**0.5+1), 2): # 제곱근 근접 숫자까지만 확인, 짝수 제외
                    if i%j == 0:
                        check = False
                        break
            if check:
                answer += 1
    return answer
