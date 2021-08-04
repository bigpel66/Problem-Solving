import sys

def input_action():
    list = []
    iter = int(sys.stdin.readline())
    for i in range(iter):
        x, y = sys.stdin.readline().split()
        list.append([int(x), y])
    return (list)

def solution(list):
    list.sort(key = lambda x : (x[0]))

def output_action(list):
    for i in list:
        sys.stdout.write(str(i[0]) + ' ' + i[1] + '\n')

def main():
    list = input_action()
    solution(list)
    output_action(list)

main()
