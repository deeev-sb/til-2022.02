# [카카오 인턴] 키패드 누르기

def solution(numbers, hand):
    answer = ''
    curL = 10 # 현재 왼손 위치, *은 10으로 지정
    curR = 11 # 현재 오른손 위치, #은 11로 지정
    num = [[1,2,3],[4,5,6],[7,8,9],[10,0,11]]
    colR, rowR, colL, rowL, colI, rowI = 0, 0, 0, 0, 0, 0
    
    
    for i in numbers:
        if ((i == 1) or (i == 4) or (i == 7)):
            answer += 'L'
            curL = i
        elif ((i == 3) or (i== 6) or (i == 9)):
            answer += 'R'
            curR = i
        else :
            # 배열에서의 현재 위치 찾기
            for a in range(len(num)):
                for b in range(len(num[a])):
                    if num[a][b] == curR:
                        colR, rowR = a,b
                    if num[a][b] == curL:
                        colL, rowL = a,b
                    if num[a][b] == i:
                        colI, rowI = a,b
            # 거리 계산
            tempR = abs(colR-colI) + abs(rowR-rowI)
            tempL = abs(colL-colI) + abs (rowL-rowI)
            if tempR == tempL:
                if hand == 'right':
                    answer += 'R'
                    curR = i
                elif hand == 'left':
                    answer += 'L'
                    curL = i
            elif tempR > tempL :
                answer += 'L'
                curL = i
            else : # tempR < tempL
                answer += 'R'
                curR = i
    
    return answer
