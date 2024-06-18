
# 배열 - 두 개 뽑아서 더하기

def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    score = [0 for _ in range(len(patterns))]

    for i, a in enumerate(answers):
        for j, p in enumerate(patterns):
            if a == p[i % len(p)]:
                score[j] += 1

    max_score = max(score)
    res = []

    for i, s in enumerate(score):
        if max_score == s:
            res.append(i + 1)

    return res


def main():
    print(solution([1,2,3,4,5]))
    print(solution([1,3,2,4,2]))


if __name__ == "__main__":
    main()
