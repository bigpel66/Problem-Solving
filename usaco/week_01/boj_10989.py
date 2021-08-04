import sys

def input_action():
    list = [0] * 10000
    iter = int(sys.stdin.readline())
    for i in range(iter):
        list[int(sys.stdin.readline()) - 1] += 1
    return (list)

def output_action(list):
    for i in range(10000):
        if list[i] != 0:
            for j in range(list[i]):
                sys.stdout.write(str(i + 1) + '\n')

def main():
    list = input_action()
    output_action(list)

main()
