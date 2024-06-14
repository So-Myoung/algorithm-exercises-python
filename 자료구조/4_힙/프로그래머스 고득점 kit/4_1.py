
# 프로그래머스 알고리즘 고득점 kit
# 힙 - 더 맵게 : Level 2

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    res = 0

    while len(scoville) > 1:
        f = heapq.heappop(scoville)
        if f < K:
            heapq.heappush(scoville, f + heapq.heappop(scoville) * 2)
            res += 1
        else:
            break

    return -1 if scoville[0] < K else res


def main():
    scoville = list(map(int, input().split()))
    K = int(input())

    print(solution(scoville, K))


if __name__ == "__main__":
    main()