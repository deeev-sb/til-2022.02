# 가장 큰 수 (스택)

def solution(num, m):
    num = str(num)
    stack = []
    answer = ''
    for n in num:
        if len(stack) == 0:
            stack.append(n)
        else:
            while stack and m > 0 and stack[-1] < n:
                stack.pop()
                m -= 1
            stack.append(n)
    if m:
        stack = stack[:-m] # 앞에 있는 큰 수는 다 제거했으므로 그냥 잘라도 됨
    for s in stack:
        answer += s
    return answer

num, m = map(int, input().split())
print(solution(num, m))