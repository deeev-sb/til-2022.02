# 아나그램 (해쉬)

def solution(str1, str2):
    list1 = []
    list2 = []
    for i in str1:
        list1.append(i)
    for i in str2:
        list2.append(i)
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return "NO"
    return "YES"

str1 = input()
str2 = input()
print(solution(str1, str2))