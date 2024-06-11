
# 큐, 덱 - 요세푸스 문제
# deque 자료 구조 사용
# popleft가 pop(0) 보다 성능이 훨배 좋으므로, deque를 사용해서 푸는게 좋다.

from collections import deque

def solution(N, K):
    dq = deque(range(1, N + 1))

    while len(dq) > 1:
        for _ in range(K - 1):
             dq.append(dq.popleft())

        dq.popleft()

    return dq[0]

def main():
    n, k = map(int, input().split())
    print(solution(n, k))

if __name__ == "__main__":
    main()