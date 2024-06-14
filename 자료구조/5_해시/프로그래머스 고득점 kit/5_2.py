
# 프로그래머스 알고리즘 고득점 kit
# 해시 - 완주하지 못한 선수 : Level 1

def solution(participant, completion):
    player = {}

    for p in participant:
        if p in player:
            player[p] += 1
        else:
            player[p] = 1

    for c in completion:
        player[c] -= 1

    for key in player.keys():
        if player[key] != 0:
            return key


def main():
    # 테스트 케이스 1
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    # 테스트 케이스 2
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
    # 테스트 케이스 3
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

    # 직접 입력
    # participant = list(input().split())
    # completion = list(input().split())
    # print(solution(participant, completion))

if __name__ == "__main__":
    main()
