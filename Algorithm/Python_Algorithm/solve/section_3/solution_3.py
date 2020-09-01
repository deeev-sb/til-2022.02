# 카드 역배치 (정올 기출)

def solution(a, b, num):
    for i in range((b-a)//2):
        num[a+i-1], num[b-i-1] = num[b-i-1], num[a+i-1]
    else:
        return num

num = list(range(1,21))
for i in range(10):
    a, b = map(int, input().split())
    num = solution(a, b, num)
else:
    print(num)