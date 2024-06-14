
# 스택 - 크레인 인형 뽑기 게임
# 2019 카카오 개발자 겨울 인턴십

def solution(board, moves):
    stack = [[] for _ in range(len(board[0]))]
    basket = []
    res = 0

    # board 배열을 역순으로 탐색하여 문제에 맞게 스택 형태 변환
    for row in range(len(board) - 1, -1, -1):
        for col in range(len(board[0])):
            if board[row][col]:
                stack[col].append(board[row][col])

    # moves
    for n in moves:
        if stack[n - 1]:
            d = stack[n - 1].pop()

            if basket and basket[-1] == d:
                basket.pop()
                res += 2
            else:
                basket.append(d)

    return(res)

def main():
    # 테스트 케이스
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))

if __name__ == "__main__":
    main()