
# 프로그래머스 알고리즘 고득점 kit
# 해시 - 폰켓몬 : Level 1

def solution(nums):
    return min(len(set(nums)), len(nums)/2)
    # return len(set(nums)) if len(nums)/2 > len(set(nums)) else len(nums)/2

def main():
    nums = list(map(int, input().split()))
    print(solution(nums))


if __name__ == "__main__":
    main()
