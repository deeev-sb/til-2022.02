# 2019 카카오 개발자 겨울 인턴십 크레인 인형뽑기 게임 

def solution(board, moves):
    answer = 0
    temp = []
    board_len = len(board[0])
    
    for i in range(len(moves)):
        for j in range(board_len):
            if board[j][moves[i]-1]:
                temp.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                if temp[-1] in temp[-2:-1]:
                    print(temp, temp[-1], temp[-2:-1])
                    temp.pop()
                    temp.pop()
                    answer += 2
                break
    return answer
