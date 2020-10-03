# 쇠막대기(스택)

def solution(x):
    cnt = 0
    stack = []
    for i in range(len(x)):
        if x[i] == '(':
            stack.append(x[i])
        else:
            stack.pop()
            if x[i-1] == '(': # 레이저인 경우
                cnt += len(stack)
            else: # 그냥 닫힌 경우
                cnt += 1
    return cnt

x = input()
print(solution(x))