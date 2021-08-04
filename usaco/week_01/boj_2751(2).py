import sys

def input_action():
    list = []
    iter = int(sys.stdin.readline().rstrip())
    for i in range(iter):
        list.append(int(sys.stdin.readline().rstrip()))
    return (list)

def max_heapify(list, cur, size):
    max = cur;
    left = cur * 2 + 1;
    right = cur * 2 + 2;
    if left < size and list[max] < list[left]:
        max = left
    if right < size and list[max] < list[right]:
        max = right
    if max != cur:
        list[max], list[cur] = list[cur], list[max]
        max_heapify(list, max, size)

def build_heap(list, size):
    iter = size // 2 - 1
    for i in range(iter, -1, -1):
        max_heapify(list, i, size)

def solution(list):
    build_heap(list, len(list))
    for i in range(len(list) - 1, -1, -1):
        list[0], list[i] = list[i], list[0]
        max_heapify(list, 0, i)

def output_action(list):
    for i in list:
        print(i)

def main():
    list = input_action()
    solution(list)
    output_action(list)

main()
