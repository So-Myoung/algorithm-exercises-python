
# 큐, 덱 - 요세푸스 문제
# queue 자료 구조 사용
# popleft가 pop(0) 보다 성능이 훨배 좋으므로, deque를 사용해서 푸는게 좋다.

def solution(N, K):
    queue = [n for n in range(1, N + 1)]

    while len(queue) > 1:
        for _ in range(K - 1):
            queue.append(queue.pop(0))

        queue.pop(0)

    return queue[0]

def main():
    n, k = map(int, input().split())
    print(solution(n, k))

if __name__ == "__main__":
    main()