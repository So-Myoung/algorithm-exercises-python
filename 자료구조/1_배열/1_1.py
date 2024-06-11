
# 코드업 6097 : 설탕 과자 뽑기

h, w = map(int, input().split())
n = int(input())

list = [[0 for _ in range(w)] for _ in range(h)]

for _ in range(n):
    l, d, x, y = map(int, input().split())

    # 가로로 둘 때
    if d == 0:
        for _ in range(l):
            list[x-1][y-1] = 1
            y += 1

    # 세로로 둘 때
    elif d == 1:
        for _ in range(l):
            list[x-1][y-1] = 1
            x += 1

for i in range(h):
    for j in range(w):
        print(list[i][j], end=' ')
    print()