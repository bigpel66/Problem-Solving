import sys

def input_action():
    list = []
    iter = int(sys.stdin.readline())
    for i in range(iter):
        list.append(int(sys.stdin.readline()))
    return (list)

def solution(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list), 1):
            if (list[i] > list[j]):
                list[i], list[j] = list[j], list[i]

def output_action(list):
    for i in list:
        sys.stdout.write(str(i) + '\n')

def main():
    list = input_action()
    solution(list)
    output_action(list)

main()
