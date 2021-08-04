import sys

def input_action():
    list = []
    for i in range(9):
        list.append(int(sys.stdin.readline()))
    return (list)

def solution(list):
    i = -1
    max = -2147483648
    enum = enumerate(list, 1)
    for ind, val in enum:
        if max < val:
            max = val
            i = ind
    return (max, i)

def output_action(max, i):
    sys.stdout.write(str(max) + '\n' + str(i))

def main():
    list = input_action()
    max, i = solution(list)
    output_action(max, i)

main()
