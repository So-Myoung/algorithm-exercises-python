
# 큐, 덱 - 기능 개발
# 프로그래머스 자료구조 고득점 kit 출제

import math

def solution(progresses, speeds):
    res = []
    cnt = 0

    n = len(progresses)

    wrk_day = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]

    pri_day = wrk_day[0]

    for i in range(n):
        if wrk_day[i] <= pri_day:
            cnt += 1
        else:
            res.append(cnt)
            cnt = 1
            pri_day = wrk_day[i]

    res.append(cnt)
    return res


def main():
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))
    print(solution(p, s))


if __name__ == "__main__":
    main()