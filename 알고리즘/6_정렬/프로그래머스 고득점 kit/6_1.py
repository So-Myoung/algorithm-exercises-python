
# 프로그래머스 알고리즘 고득점 kit
# 정렬 - K번째 수

def solution(array, commands):

    res = []

    for cmd in commands:
        arr = sorted(array[cmd[0]-1:cmd[1]])
        res.append(arr[cmd[2]-1])

    return res


def main():
    # 테스트 케이스 1
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


if __name__ == "__main__":
    main()
