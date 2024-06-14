
# 힙 프로그램 구현

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        return heapq.heappop(self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)

    def push_tuple(self, value):
        # 튜플 (우선순위, 값) 로 우선 순위 지정 가능
        heapq.heappush(self.heap, (-value, value))

    def pop_tuple(self):
        return heapq.heappop(self.heap)


def main():
    print('-----최소힙-----')
    min = MinHeap()
    min.push(10)
    min.push(5)
    min.push(20)
    min.push(1)
    print(min.heap) # heapq는 꺼내면서 정렬을 하기 때문에 정렬된 상태가 아님
    print(min.pop())
    print(min.heap) # 정렬 상태
    print(min.pop())
    print(min.heap)

    print('-----최대힙-----')
    max = MaxHeap()
    max.push(10)
    max.push(5)
    max.push(20)
    max.push(1)
    print([max.pop() for _ in range(len(max.heap))])

    print('-----최대힙(튜플 삽입)-----')
    max = MaxHeap()
    max.push_tuple(10)
    max.push_tuple(5)
    max.push_tuple(20)
    max.push_tuple(1)
    print(max.heap) # (우선순위, 값)
    print([max.pop_tuple()[1] for _ in range(len(max.heap))]) # index 1 = 값 출력

if __name__ == "__main__":
    main()