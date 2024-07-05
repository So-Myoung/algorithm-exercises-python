
# 그리디 - 큰 수의 법칙
# 반복되는 수열(규칙) 파악

result = 0
n, m, k = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort()
first = n_list[n - 1]
second = n_list[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
# 규칙이 끝나고 남은 횟수를 큰 수 횟수에 더하기
count += m % (k + 1)

# 첫번째로 큰 수 sum
result += (count) * first
# 두번째로 큰 수 sum
result += (m - count) * second

print(result)
