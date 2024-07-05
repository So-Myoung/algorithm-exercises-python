
#프로그래머스 알고리즘 고득점 kit
# 힙 - 이중 우선 순위 큐 : Level 3


import heapq


def solution(operations):
    heap = []

    for op in operations:
        cmd = op.split(' ')

        if cmd[0] == 'I':
            heapq.heappush(heap, int(cmd[1]))
        elif cmd[1] == '-1' and heap:
            heapq.heappop(heap)
        elif cmd[1] == '1' and heap:
            heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heapq.heappop(heap)]


def main():
    # 테스트 케이스 1
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    # 테스트 케이스 2
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))


if __name__ == "__main__":
    main()
