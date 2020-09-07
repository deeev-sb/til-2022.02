# 카드 역배치 (정올 기출)

def solution(a, b, num):
    for i in range((b-a+1)//2):
        num[a+i], num[b-i] = num[b-i], num[a+i]
    return num

num = list(range(21))
for i in range(10):
    a, b = map(int, input().split())
    num = solution(a, b, num)


for i in range(1, 21):
    print(num[i], end = ' ')