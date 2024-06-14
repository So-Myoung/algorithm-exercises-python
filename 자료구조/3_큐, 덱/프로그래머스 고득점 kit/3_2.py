
# 프로그래머스 알고리즘 고득점 kit
# 큐, 덱 - 다리를 지나는 트럭 : Level 2

from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    time = 0

    # 방법 1. truck_weights를 순회
    while truck_weights:
        bridge_weight -= bridge.popleft()
        time += 1

        if bridge_weight + truck_weights[0] <= weight:
            t = truck_weights.popleft()
            bridge.append(t)
            bridge_weight += t
        else:
            bridge.append(0)

    # 마지막 트럭이 append 되고 반복문이 종료되기 때문에, bridge_length만큼 밀어주어 다리를 건너게한다.
    time += bridge_length

    return time

    # 방법 2. bridge를 순회
    # while bridge:
    #     bridge_weight -= bridge.popleft()
    #     time += 1
    #
    #     # truck_weight에 요소가 없으면(더 이상 보낼 트럭이 없으면) bridge에 트럭을 추가하지 않는다.
    #     # bridge_weight -= bridge.popleft() 이 코드에 의해 먼저 들어온 값이 차례로 pop되고, 마지막 트럭이 다리를 건너는 순간 반복문을 탈출한다.
    #     if truck_weights:
    #         if bridge_weight + truck_weights[0] <= weight:
    #             t = truck_weights.popleft()
    #             bridge.append(t)
    #             bridge_weight += t
    #         else:
    #             bridge.append(0)
    #
    # return time

    # 결론 -> 방법 1은 마지막 트럭이 다리 맨 끝에 들어오는(append) 순간 반복문을 탈출하고, time에 다리의 길이만큼 더해준다. 시간 복잡도 + O(1)
    # 반면에 방법 2는 마지막 트럭이 들어오고 다리의 길이만큼 반복문을 반복한 후 bridge의 length가 0이 되면 반복문을 탈출한다. 시간 복잡도 + O(N), 이 때 N은 다리의 길이(bridge_length)
    # 그러므로 시간 복잡도나 루프 횟수도 적고, 좀 더 직관적인 방법 1을 선택하기로 하였다.


def main():
    # 테스트 케이스 1
    print(solution(2, 10, [7, 4, 5, 6]))
    # 테스트 케이스 2
    print(solution(100, 100, [10]))
    # 테스트 케이스 3
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))


if __name__ == "__main__":
    main()
