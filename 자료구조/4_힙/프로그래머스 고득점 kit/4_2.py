
# 프로그래머스 알고리즘 고득점 kit
# 힙 - 디스크 컨트롤러 : Level 3

import heapq


def solution(jobs):
    now_time = 0  # 현재 시간
    finish_work_start = -1  # 마지막 완료 작업의 시작 시간
    total_time = 0
    finish_work = 0  # 작업 처리 개수
    heap = []

    while finish_work < len(jobs):
        for job in jobs:
            if finish_work_start < job[0] <= now_time:
                heapq.heappush(heap, [job[1], job[0]])

        if heap:
            # heap = default 오름차순 정렬이기 때문에, 작업이 가능한 항목 중 처리 시간이 더 짧은 작업을 작업하도록 한다.
            now_working = heapq.heappop(heap)

            finish_work_start = now_time
            now_time += now_working[0]

            total_time += (now_time - now_working[1])
            finish_work += 1
        else:
            now_time += 1

    return int(total_time / len(jobs))


def main():
    # 테스트 케이스 1
    print(solution([[0, 3], [1, 9], [2, 6]]))


if __name__ == "__main__":
    main()
