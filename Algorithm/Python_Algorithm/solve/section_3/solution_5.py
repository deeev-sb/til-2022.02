# 수들의 합
# 5번 테스트 케이스가 타임아웃이 떠서 풀이과정에 대한 설명을 들은 후 풀었음

def solution(N, M, num):
    count, left, right = 0, 0, 1
    total = num[0]
    while True:
        if left == N:
            break
        elif total < M:
            if right == N:
                break
            else:
                total += num[right]
                right += 1
        elif total == M:
            count += 1
            total -= num[left]
            left += 1
        else:
            total -= num[left]
            left += 1
    return count

N, M = map(int, input().split())
num = list(map(int, input().split()))
print(solution(N, M, num))