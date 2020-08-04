# 전화번호 목록

def solution(phone_book):
    answer = True
    
    phone_book = sorted(phone_book)
    
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] in phone_book[j][0:len(phone_book[i])]:
                return False
    
    return answer
