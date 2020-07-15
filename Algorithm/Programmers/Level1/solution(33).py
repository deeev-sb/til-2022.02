# 모의고사

def solution(answers):
    answer = []
    student1=[1, 2, 3, 4, 5]
    student2=[2, 1, 2, 3, 2, 4, 2, 5]
    student3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1 , count2, count3 = 0, 0, 0
    
    for i in range(len(answers)):
        j = i%len(student1)
        if answers[i] == student1[j]:
            count1 += 1
    
    for i in range(len(answers)):
        j = i%len(student2)
        if answers[i] == student2[j]:
            count2 += 1
    
    for i in range(len(answers)):
        j = i%len(student3)
        if answers[i] == student3[j]:
            count3 += 1
    
    max_answer = max(count1, count2, count3)
    
    if count1 == max_answer:
        answer.append(1)
    if count2 == max_answer:
        answer.append(2)
    if count3 == max_answer:
        answer.append(3)
    
    return answer
