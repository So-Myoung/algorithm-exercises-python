
# 정렬 - 계수 정렬 구현하기

def solution(s):
    cnt = [0 for _ in range(ord('z') - ord('a') + 1)]
    res = ''

    for c in s:
        cnt[ord(c) - ord('a')] += 1

    for i in range(len(cnt)):
        res += chr(ord('a') + i) * cnt[i]

    return res


def main():
    s = input()
    print(solution(s))


if __name__ == "__main__":
    main()