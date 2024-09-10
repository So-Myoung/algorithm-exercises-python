# 프로그래머스 알고리즘 고득점 kit - 폰켓몬

def solution(nums):
    # n = len(set(nums))  # 폰켓몬의 종류
    # k = len(nums) / 2  # 가져갈 수 있는 폰켓몬의 수
    return min(len(set(nums)), len(nums) / 2)


def main():
    # 테스트 케이스 1
    print(solution([3,1,2,3]))
    # 테스트 케이스 2
    print(solution([3,3,3,2,2,4]))
    # 테스트 케이스 3
    print(solution([3,3,3,2,2,2]))


if __name__ == "__main__":
    main()
