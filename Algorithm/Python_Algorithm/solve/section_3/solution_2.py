# 숫자만 추출

def solution(text):
    len_text = len(text)
    answer = ''
    count = 0
    for i in range(len_text):
        if text[i].isdigit():
            answer += text[i]
    answer = int(answer)
    for i in range(1, answer+1):
        if answer%i==0 :
            count += 1
    print(answer, count, sep='\n')

text = input()
solution(text)