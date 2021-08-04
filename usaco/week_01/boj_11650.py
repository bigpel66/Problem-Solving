import sys

def input_action():
    list = []
    iter = int(sys.stdin.readline())
    for i in range(iter):
        x, y = map(int, sys.stdin.readline().split())
        list.append([x, y])
    return (list)

def solution(list):
    list.sort(key = lambda x : (x[0], x[1]))

def output_action(list):
    for i in list:
        sys.stdout.write(str(i[0]) + ' ' + str(i[1]) + '\n')

def main():
    list = input_action()
    solution(list)
    output_action(list)

main()
