# 후위 표기식 만들기 (스택)

def solution(s):
    answer = ''
    stack = []
    for i in s:
        if i.isdecimal():
            answer += i
        elif i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(': # '(' 직전까지 pop()
                answer += stack.pop()
            stack.pop() # '(' 제거
    while stack:
        answer += stack.pop()
    return answer

s = input()
print(solution(s))