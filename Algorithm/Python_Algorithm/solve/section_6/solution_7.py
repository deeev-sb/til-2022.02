# 동전교환

def DFS(cnt, p): # cnt는 DFS가 수행된 횟수(동전 수), p는 현재 금액
    global min_cnt
    if cnt > min_cnt:
        return
    if p > m:
        return
    if p == m and cnt < min_cnt:
        min_cnt = cnt
    else:
        for i in range(n):
            DFS(cnt + 1, p + kind[i])
    

if __name__ == "__main__":
    n = int(input())
    kind = list(map(int, input().split()))
    m = int(input())
    min_cnt = 2147000000 # int에서 가질 수 있는 대략적인 max 값
    kind.reverse()
    DFS(0, 0)
    print(min_cnt)

# 그리디 구현할 경우 최소라는 조건을 충족하지 못함
# def solution(n, kind, m):
#     kind.reverse()
#     cnt = 0
#     for i in range(n):
#         if m >= kind[i]:
#             cnt = cnt + (m // kind[i])
#             m %= kind[i]
#     return cnt

# n = int(input())
# kind = list(map(int, input().split()))
# m = int(input())
# print(solution(n, kind, m))
