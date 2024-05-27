
# 실전문제 1-1
# 그리드 - 큰 수의 법칙 : 난이도 1
# 1-1-1. 단순하게 풀기

result = 0
n, m, k = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort()
first = n_list[n - 1]
second = n_list[n - 2]

while 1:
    for i in range(k):
        if m == 0:
            break;
        result += first
        m -= 1

    if m == 0 :
        break

    result += second
    m -= 1

print(result)