
# 정렬 - 성적이 낮은 순서로 학생 출력하기

n = int(input())
dic = {}

for _ in range(n):
    info = input().split()
    dic[info[0]] = int(info[1])

# items() -> key, value가 tuple로 들어 있는 리스트 생성
# ex) [('홍길동', 95), ('이순신', 77)]
res = sorted(dic.items(), key=lambda x: x[1])

for r in res:
    print(r[0], end=' ')