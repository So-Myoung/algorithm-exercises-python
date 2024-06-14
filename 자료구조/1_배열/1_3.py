
# 배열 - 두 개 뽑아서 더하기

def solution(numbers):
    res = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            res.append(numbers[i]+numbers[j])

    return sorted(set(res))

def main():
    numbers = list(map(int, input().split()))
    print(solution(numbers))


if __name__ == "__main__":
    main()
