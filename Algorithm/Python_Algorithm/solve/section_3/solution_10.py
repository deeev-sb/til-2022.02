# 스도쿠 검사

def solution(sudoku):
    for i in range(9):
        if len(list(set(sudoku[i]))) != 9:
            return "NO"
        else:
            temp = set()
            for j in range(9):
                temp.add(sudoku[j][i])
            if len(list(temp)) != 9:
                return "NO"
    else:
        start, end = 0, 3
        for _ in range(3):
            temp = []
            for i in range(start, end):
                for j in range(start, end):
                    temp.append(sudoku[i][j])
            if len(list(set(temp))) != 9:
                return "NO"
            start += 3
            end += 3
        else:
            return "YES"

sudoku = [list(map(int, input().split())) for _ in range(9)]
print(solution(sudoku))
