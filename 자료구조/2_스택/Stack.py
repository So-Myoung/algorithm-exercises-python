
# 스택 프로그램 구현

class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size
        self.top = -1

    def isFull(self, item):
        return len(self.stack) == self.max_size

    def isEmpty(self, item):
        return len(self.stack) == 0

    def push(self, item):
        if self.isFull(self.stack):
            print("!!Stack Full!!")
        else:
            self.top += 1
            self.stack.append(item)

    def pop(self):
        if self.isEmpty(self.stack):
            print("Stack Empty")
        else:
            self.top -= 1
            self.stack.pop()

    def peek(self):
        print(f'Current Top Index >>> {self.top}')
        print(f'Current Top Value >>> {self.stack[self.top]}')

    def list_show(self):
        for i, v in reversed(list(enumerate(self.stack))):
            print(f'{i}번 index : {v}')

def main():
    s = Stack(10)
    s.push(5)
    s.push(8)
    s.push(4)
    s.push(5)
    s.push(2)
    s.push(11)
    s.push(8)
    s.push(4)
    s.push(5)
    s.push(2)

    # 결과 출력
    s.peek()
    s.list_show()

if __name__ == "__main__":
    main()