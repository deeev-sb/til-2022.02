# 후위 연산 (스택)

def solution(s):
    stack = []
    for i in s:
        if i.isdecimal():
            stack.append(int(i))
        elif i == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2*num1)
        elif i == '/':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2/num1)
        elif i == '+':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2+num1)
        elif i == '-':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2-num1)
    return stack[0]

s = input()
print(solution(s))