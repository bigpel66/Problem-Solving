import sys

def input_action():
    iter = int(sys.stdin.readline())
    nums = list(map(int, (sys.stdin.readline().split())))
    return (nums[:iter])

def solution(list):
    min, max = 2147483647, -2147483648
    for i in list:
        if min > i:
            min = i
        if max < i:
            max = i
    return (min, max)

def output_action(min, max):
    sys.stdout.write(str(min) + ' ' + str(max))

def main():
    list = input_action()
    min, max = solution(list)
    output_action(min, max)

main()
