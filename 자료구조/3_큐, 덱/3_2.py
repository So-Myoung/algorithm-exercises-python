
# 큐, 덱 - 카드 뭉치

from collections import deque


def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else:
            break

    # if goal:
    #     return "No"
    # else:
    #     return "Yes"
    return "Yes" if not goal else "No"  # 삼항 연산자


def main():
    # 테스트 케이스 1
    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
    # 테스트 케이스 2
    print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))

    # 직접 입력
    # c1 = deque(input().split())
    # c2 = deque(input().split())
    # g = deque(input().split())
    # print(solution(c1, c2, g))


if __name__ == "__main__":
    main()
