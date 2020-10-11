# 재귀함수를 이용한 이진수 출력

def solution(num):
    answer = ''
    while num:
        answer = str(num%2) + answer
        num = num // 2
    return answer

num = int(input())
print(solution(num))