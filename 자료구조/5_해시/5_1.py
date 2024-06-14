
# 해시 - 두 개의 수로 특정 값 만들기
# 조건 고려 - arr 에서 중복 되는 원소는 없음.
# x + k = target이 되는 x, k가 arr에 존재하면 true

def hash_table(arr, target):
    table = [0 for _ in range(target + 1)]

    for n in arr:
        if n <= target:
            table[n] = 1

    return table


def solution(arr, target):
    table = hash_table(arr, target)

    for x in arr:
        k = target - x
        if k != x and 0 <= k <= target and table[k] == 1:
            return True

    return False


def main():
    arr = list(map(int, input().split()))
    target = int(input())
    print(solution(arr, target))


if __name__ == "__main__":
    main()
