# 2016년

def solution(a, b):
    answer = ''
    day_name = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month_end = [31,29,31,30,31,30,31,31,30,31,30,31]
    month_sum = b
    for i in range(a-1):
        month_sum += month_end[i]
    answer = day_name[month_sum%7-1]
    return answer
