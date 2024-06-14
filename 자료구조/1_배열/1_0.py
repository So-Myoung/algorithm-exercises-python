
# 배열 - 배열 제어하기

# 1. sort()
# 리스트 전용 메소드로 리스트명.sort() 형식으로 사용
# 리스트 원본값을 직접 수정

# 2. sorted()
# 내장함수이며, 리스트 외에도 이터러블 객체이면 사용할 수 있음
# sorted(리스트명) 형식으로 사용함
# 리스트 원본 값은 그대로이고 정렬 값을 반환함

# 3. reverse
# list.sort()와 내장함수 sorted()는 모두 reverse 매개변수를 받는다.
# sort(reverse = True), sorted(이터러블 객체, reverse=True) -> 내림차순
# +) 리스트.reverse() = 정렬이 아닌 단순 리스트 순서 뒤집기

def solution(numbers):
    # res = list(set(numbers)) # set(집합) 자료형을 써서 중복을 제거한 후, sort 함수를 쓰기 위해 list 형태로 변경
    # res.sort(reverse=True)

    # return res
    return sorted(set(numbers), reverse=True) # 정답 한 줄로 표현 하기

def main():
    numbers = list(map(int, input().split()))
    print(solution(numbers))


if __name__ == "__main__":
    main()
