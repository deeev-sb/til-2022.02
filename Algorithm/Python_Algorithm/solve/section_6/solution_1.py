# 재귀함수를 이용한 이진수 출력


# def solution(num):
#     answer = ''
#     while num:
#         answer = str(num%2) + answer
#         num = num // 2
#     return answer

# 재귀함수를 사용하지 않아서 다시 작성

def solution(answer, num):
    if num == 0:
        print(answer)
    else:
        answer = str(num%2) + answer
        solution(answer, num//2)

num = int(input())
answer = ''
solution(answer, num)