import sys

def input_action():
    iter = int(sys.stdin.readline().rstrip())
    list = []
    for i in range(iter):
        list.append(int(input()))
    return (list)

def solution(list):
    if len(list) <= 1:
        return (list)
    mid = len(list) // 2
    left = solution(list[:mid])
    right = solution(list[mid:])
    i = 0
    j = 0
    tmp = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            i += 1
        else :
            tmp.append(right[j])
            j += 1
    while i < len(left):
        tmp.append(left[i])
        i += 1
    while j < len(right):
        tmp.append(right[j])
        j += 1
    return (tmp)

def output_action(list):
    for i in list:
        print(i)

def main():
    list = input_action()
    list = solution(list)
    output_action(list)

main()
