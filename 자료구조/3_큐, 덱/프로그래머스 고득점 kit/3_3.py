
# 프로그래머스 알고리즘 고득점 kit
# 큐, 덱 - 프로세스 : Level 2

from collections import deque


def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    res = 0
    while True:
        cur = deque.popleft(queue)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            res += 1
            if cur[0] == location:
                return res


def main():
    # 테스트 케이스 1
    print(solution([2, 1, 3, 2], 2))
    # 테스트 케이스 2
    print(solution([1, 1, 9, 1, 1, 1], 0))


if __name__ == "__main__":
    main()
