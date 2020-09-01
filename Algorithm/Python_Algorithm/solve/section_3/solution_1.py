# 회문 문자열 검사

def solution(data):
    len_data = len(data) -1
    data = data.lower()
    for i in range(len_data, -1, -1):
        if data[i] != data[len_data - i]:
            return "NO"
    else:
        return "YES"

N = int(input())
for i in range(N):
    data = input()
    print("#", (i+1), ' ', solution(data), sep='')